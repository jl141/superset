/**
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */
import { SupersetClient, t } from '@superset-ui/core';
import { SelectOption } from 'src/components/ListView';
import { FormValues } from './types';

export const softDeleteUser = async (user_Id: number) => {
  await SupersetClient.post({
    endpoint: `/api/v1/security/users/soft_delete/${user_Id}`
  })
}

export const createUser = async (values: FormValues) => {
  const { confirmPassword, ...payload } = values;
  if (payload.active == null) {
    payload.active = false;
  }
  await SupersetClient.post({
    endpoint: '/api/v1/security/users/',
    jsonPayload: { ...payload },
  });
};

export const updateUser = async (user_Id: number, values: FormValues) => {
  await SupersetClient.put({
    endpoint: `/api/v1/security/users/${user_Id}`,
    jsonPayload: { ...values },
  });
};

export const deleteUser = async (userId: number) =>
  SupersetClient.delete({
    endpoint: `/api/v1/security/users/${userId}`,
  });

export const getUserAssets = async (userId: number) => {
  const params = JSON.stringify({
    filters: [{ col: 'owners', opr: 'rel_m_m', value: userId }],
  });

  const [dashboards, charts, datasets] = await Promise.all([
    SupersetClient.get({
      endpoint: `/api/v1/dashboard/?q=${params}`,
    }),
    SupersetClient.get({
      endpoint: `/api/v1/chart/?q=${params}`,
    }),
    SupersetClient.get({
      endpoint: `/api/v1/dataset/?q=${params}`,
    }),
  ]);

  return {
    dashboards: dashboards.json?.result || [],
    charts: charts.json?.result || [],
    datasets: datasets.json?.result || [],
  };
};

export const reassignUserAssets = async (
  userId: number,
  newOwnerId: number,
  assetType: 'dashboard' | 'chart' | 'dataset',
  assets: Array<{ id: number; owners?: Array<{ id: number }> }>,
) => {
  const promises = assets.map(asset => {
    const currentOwners = asset.owners || [];
    const ownerIds = currentOwners.map(owner => owner.id);

    // Remove old owner and add new owner
    const updatedOwnerIds = ownerIds.filter(id => id !== userId);
    if (!updatedOwnerIds.includes(newOwnerId)) {
      updatedOwnerIds.push(newOwnerId);
    }

    const endpoint =
      assetType === 'dashboard'
        ? `/api/v1/dashboard/${asset.id}`
        : assetType === 'chart'
          ? `/api/v1/chart/${asset.id}`
          : `/api/v1/dataset/${asset.id}`;

    return SupersetClient.put({
      endpoint,
      jsonPayload: { owners: updatedOwnerIds },
    });
  });

  return Promise.all(promises);
};

export const atLeastOneRoleOrGroup =
  (fieldToCheck: 'roles' | 'groups') =>
  ({
    getFieldValue,
  }: {
    getFieldValue: (field: string) => Array<SelectOption>;
  }) => ({
    validator(_: object, value: Array<SelectOption>) {
      const current = value || [];
      const other = getFieldValue(fieldToCheck) || [];
      if (current.length === 0 && other.length === 0) {
        return Promise.reject(
          new Error(t('Please select at least one role or group')),
        );
      }
      return Promise.resolve();
    },
  });
