# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname kubernetes

Name:           python-%{srcname}
Version:        36.0.2
Release:        %autorelease
Summary:        Kubernetes python client
License:        Apache-2.0
URL:            https://github.com/kubernetes-client/python
VCS:            git:https://github.com/kubernetes-client/python.git
#!RemoteAsset:  sha256:03551fcb49cae1f708f63624041e37403545b7aaed10cbf54e2b01a37a5438e3
Source0:        https://files.pythonhosted.org/packages/source/k/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
# test modules shipped inside the package import pytest and mock
BuildOption(check):  -e 'kubernetes.*_test' -e 'kubernetes.*.test_*'
# kubernetes.aio needs aiohttp, which upstream treats as optional
BuildOption(check):  -e 'kubernetes.aio*'
# demo script, loads kube config at import time
BuildOption(check):  -e 'kubernetes.leaderelection.example'

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Python client for the kubernetes API. It allows users to interact with
a Kubernetes cluster from Python: manage resources, watch for changes,
load cluster and kubeconfig based configuration.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
