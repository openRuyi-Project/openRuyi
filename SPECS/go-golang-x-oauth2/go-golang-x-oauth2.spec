# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           oauth2
%define go_import_path  golang.org/x/oauth2
# circular dependency with google.golang.org/cloud
%define go_test_exclude_glob golang.org/x/oauth2/google*

Name:           go-golang-x-oauth2
Version:        0.34.0
Release:        %autorelease
Summary:        Go supplementary network libraries
License:        BSD-3-Clause
URL:            https://golang.org/x/oauth2
VCS:            git:https://github.com/golang/oauth2
#!RemoteAsset:  sha256:7b5aa72ed4631661a3a8fafbc779724296b57d946bd2c0d5e513e48c8e83329f
Source0:        https://github.com/golang/oauth2/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)

Provides:       go(golang.org/x/oauth2) = %{version}

Requires:       go(github.com/google/go-cmp)

%description
This repository holds supplementary Go networking packages.

# We need to split google specific code into a subpackage
# In order to avoid circular dependency
%package        google
Summary:        Google specific OAuth2 support

Provides:       go(golang.org/x/oauth2/google) = %{version}

# Use the specific golang import path for google subpackage
Requires:       go(cloud.google.com/go/compute/metadata)

%description    google
This package provides support for making OAuth2 authorized and
authenticated HTTP requests against Google APIs. It can additionally grant
authorization with Bearer JWT.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}
%exclude %{go_sys_gopath}/%{go_import_path}/google

%files google
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}/google

%changelog
%autochangelog
