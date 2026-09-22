# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           pkg
%define go_import_path  yunion.io/x/pkg
%define commit_id       6008459eb4f0a293eff95ac7aca077fa7401969d

Name:           go-yunion-x-pkg
Version:        0+git20260922.6008459
Release:        %autorelease
Summary:        Common Go utilities for Cloudpods
License:        Apache-2.0
URL:            https://github.com/yunionio/pkg
#!RemoteAsset:  sha256:b2bee359dd8ed9d0dca16c9cd04ef41b5332e6d8a977c73640113ae88ea1919c
Source0:        https://github.com/yunionio/pkg/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Current Go vet rejects variable format strings in compare and trace.
BuildOption(check):  -vet=off
# The delayed-work test races its asynchronous callback and assumes a
# 50 ms scheduling margin, which fails under load on both OBS architectures.
BuildOption(check):  -skip '^TestDelayedWork$'

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  tzdata
BuildRequires:  go(github.com/fatih/color)
BuildRequires:  go(github.com/gin-gonic/gin)
BuildRequires:  go(github.com/golang-plus/uuid)
BuildRequires:  go(github.com/ma314smith/signedxml)
BuildRequires:  go(github.com/mozillazg/go-pinyin)
BuildRequires:  go(github.com/pkg/errors)
BuildRequires:  go(github.com/prometheus/client_golang)
BuildRequires:  go(github.com/tredoe/osutil)
BuildRequires:  go(github.com/ulikunitz/xz)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(moul.io/http2curl/v2)
BuildRequires:  go(yunion.io/x/jsonutils)
BuildRequires:  go(yunion.io/x/log)

Provides:       go(yunion.io/x/pkg) = %{version}

Requires:       go-yunion-x-pkg-support = %{version}
Requires:       go(github.com/fatih/color)
Requires:       go(github.com/gin-gonic/gin)
Requires:       go(github.com/golang-plus/uuid)
Requires:       go(github.com/ma314smith/signedxml)
Requires:       go(github.com/mozillazg/go-pinyin)
Requires:       go(github.com/pkg/errors)
Requires:       go(github.com/prometheus/client_golang)
Requires:       go(github.com/tredoe/osutil)
Requires:       go(github.com/ulikunitz/xz)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/text)
Requires:       go(moul.io/http2curl/v2)
Requires:       go(yunion.io/x/jsonutils)
Requires:       go(yunion.io/x/log)

%description
This package provides common Cloudpods utilities for networking, storage,
HTTP clients, validation and data conversion. Base helpers are supplied
by the matching support package to break the jsonutils dependency cycle.

%prep -a
rm -rf vendor

%install -a
# These directories are owned by the matching support package.
rm -rf %{buildroot}%{go_sys_gopath}/%{go_import_path}/errors
rm -rf %{buildroot}%{go_sys_gopath}/%{go_import_path}/gotypes
rm -rf %{buildroot}%{go_sys_gopath}/%{go_import_path}/sortedmap
rm -rf %{buildroot}%{go_sys_gopath}/%{go_import_path}/tristate
rm -rf %{buildroot}%{go_sys_gopath}/%{go_import_path}/util/reflectutils
rm -rf %{buildroot}%{go_sys_gopath}/%{go_import_path}/util/regutils
rm -rf %{buildroot}%{go_sys_gopath}/%{go_import_path}/util/signalutils
rm -rf %{buildroot}%{go_sys_gopath}/%{go_import_path}/util/timeutils
rm -rf %{buildroot}%{go_sys_gopath}/%{go_import_path}/utils

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
