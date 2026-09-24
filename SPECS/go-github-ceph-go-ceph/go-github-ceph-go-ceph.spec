# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-ceph
%define go_import_path  github.com/ceph/go-ceph
%define go_test_include %{go_import_path}/rados

Name:           go-github-ceph-go-ceph
Version:        0+git20181217.e32f9f0
Release:        %autorelease
Summary:        Is the root of a set of packages that wrap the Ceph APIs
License:        MIT
URL:            https://github.com/ceph/go-ceph
VCS:            git:https://github.com/ceph/go-ceph.git
#!RemoteAsset:  sha256:5cfa234b0d840b76d8ab865a0b697bdda795f08b62933c3d0306ae956ddba3b3
Source0:        https://github.com/ceph/go-ceph/archive/e32f9f0f2e94.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n go-ceph-e32f9f0f2e941422937c0a6c4f0a61b8f0c82995
# The rados tests require a live Ceph cluster. Compile the imported package and
# its tests in OBS without attempting an external cluster connection.
BuildOption(check):  -run '^$'

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  ceph-devel
BuildRequires:  go(github.com/gofrs/uuid)
BuildRequires:  go(github.com/sirupsen/logrus)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/ceph/go-ceph) = %{version}

Requires:       go(github.com/sirupsen/logrus)

%description
This package provides the github.com/ceph/go-ceph Go module source.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
