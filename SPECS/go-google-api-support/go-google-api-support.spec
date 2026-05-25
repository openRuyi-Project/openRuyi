# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           api
%define go_import_path  google.golang.org/api

Name:           go-google-api-support
Version:        0.280.0
Release:        %autorelease
Summary:        Bootstrap support packages for google.golang.org/api
License:        Apache-2.0
URL:            https://github.com/googleapis/google-api-go-client
#!RemoteAsset:  sha256:bad3e08b3e0da8446e016077facf63927317079c1d5636a0dbe6d3a39b8e2a76
Source0:        https://github.com/googleapis/google-api-go-client/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n google-api-go-client-0.280.0
# These leaf packages are needed to break the google-api <-> gax-go bootstrap
# cycle. They do not import gax-go or google-cloud-go, so they can be built
# before the full go-google-api package.
%define go_test_include %{shrink:
    %{go_import_path}/googleapi
    %{go_import_path}/internal/third_party/uritemplates
    %{go_import_path}/iterator
}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(google.golang.org/api/googleapi) = %{version}
Provides:       go(google.golang.org/api/googleapi/transport) = %{version}
Provides:       go(google.golang.org/api/internal/third_party/uritemplates) = %{version}
Provides:       go(google.golang.org/api/iterator) = %{version}
Provides:       go(google.golang.org/api/iterator/testing) = %{version}

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
