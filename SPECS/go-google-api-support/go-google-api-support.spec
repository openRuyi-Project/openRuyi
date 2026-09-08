# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           api
%define go_import_path  google.golang.org/api
# These leaf packages are needed to break the google-api <-> gax-go bootstrap
# cycle. They do not import gax-go or google-cloud-go, so they can be built
# before the full go-google-api package. - HNO3Miracle
%define go_test_include %{shrink:
    %{go_import_path}/googleapi
    %{go_import_path}/internal/third_party/uritemplates
    %{go_import_path}/iterator
}

Name:           go-google-api-support
Version:        0.297.0
Release:        %autorelease
Summary:        Bootstrap support packages for google.golang.org/api
License:        Apache-2.0
URL:            https://github.com/googleapis/google-api-go-client
#!RemoteAsset:  sha256:badf4fce9c37b452bcc0e69ce4efd740841364d3a6ad0b90d2fe6d684c80c39b
Source0:        https://github.com/googleapis/google-api-go-client/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(google.golang.org/api/googleapi) = %{version}
Provides:       go(google.golang.org/api/internal/third_party/uritemplates) = %{version}
Provides:       go(google.golang.org/api/iterator) = %{version}

%description
This package provides bootstrap support packages for google.golang.org/api.

%install
install -d %{buildroot}%{go_sys_gopath}/%{go_import_path}/internal/third_party
cp -a googleapi %{buildroot}%{go_sys_gopath}/%{go_import_path}/googleapi
cp -a iterator %{buildroot}%{go_sys_gopath}/%{go_import_path}/iterator
cp -a internal/third_party/uritemplates %{buildroot}%{go_sys_gopath}/%{go_import_path}/internal/third_party/uritemplates

%check
%buildsystem_golangmodules_check

%files
%license LICENSE
%{go_sys_gopath}/%{go_import_path}/googleapi
%{go_sys_gopath}/%{go_import_path}/internal
%{go_sys_gopath}/%{go_import_path}/iterator

%changelog
%autochangelog
