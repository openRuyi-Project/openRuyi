# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname tritonclient
%global commit_hash 31c9421d4b0c2acbe9d9d214067ed74b7db4b6ae

Name:           python-%{srcname}
Version:        2.67.0
Release:        %autorelease
Summary:        Python client library and utilities for communicating with Triton Inference Server
License:        BSD-3-Clause
URL:            https://developer.nvidia.com/dynamo-triton
VCS:            git:https://github.com/triton-inference-server/client.git
# PyPI only provides binary wheels; using source from GitHub for building.
#!RemoteAsset:  sha256:ffe04297656f38a9ed732e87a9f4621db6f3f926687f1901c7b13334ea498abb
Source0:        https://github.com/triton-inference-server/client/archive/%{commit_hash}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l tritonclient tritonclientutils tritongrpcclient tritonhttpclient tritonshmutils
# No module named 'CUDA'
BuildOption(check):  -e tritonclient.utils.cuda_shared_memory
BuildOption(check):  -e tritonclient.grpc*
BuildOption(check):  -e tritongrpcclient
BuildOption(check):  -e tritongrpcclient.model_config_pb2
BuildOption(check):  -e tritongrpcclient.grpc_service*
BuildOption(check):  -e tritonshmutils.cuda*

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Python client library and utilities for communicating with Triton Inference Server.

%pyproject_extras_subpkg -n python-tritonclient http

%prep -a
rm -f pyproject.toml
mv src/python/library/* .

%generate_buildrequires
export VERSION=%{version}
%pyproject_buildrequires -x http

%build -p
export VERSION=%{version}

%install -p
shopt -s nullglob
export VERSION=%{version}

%install -a
# Remove the tests directory that is incorrectly installed.
rm -rf %{buildroot}%{python3_sitelib}/tests/
# Remove redundant licenses.
rm -f %{buildroot}/usr/LICENSE.txt

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
