# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           pkg
%define go_import_path  yunion.io/x/pkg
%define commit_id       6008459eb4f0a293eff95ac7aca077fa7401969d

# jsonutils and executor need these helpers; they do not import jsonutils.
%define go_test_include %{shrink:
    %{go_import_path}/errors
    %{go_import_path}/gotypes
    %{go_import_path}/sortedmap
    %{go_import_path}/tristate
    %{go_import_path}/util/reflectutils
    %{go_import_path}/util/regutils
    %{go_import_path}/util/signalutils
    %{go_import_path}/util/timeutils
    %{go_import_path}/utils
}

Name:           go-yunion-x-pkg-support
Version:        0+git20260922.6008459
Release:        %autorelease
Summary:        Base Go helpers for the Cloudpods dependency bootstrap
License:        Apache-2.0
URL:            https://github.com/yunionio/pkg
#!RemoteAsset:  sha256:b2bee359dd8ed9d0dca16c9cd04ef41b5332e6d8a977c73640113ae88ea1919c
Source0:        https://github.com/yunionio/pkg/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  tzdata
BuildRequires:  go(github.com/pkg/errors)
BuildRequires:  go(yunion.io/x/log)

Provides:       go(yunion.io/x/pkg/errors) = %{version}
Provides:       go(yunion.io/x/pkg/gotypes) = %{version}
Provides:       go(yunion.io/x/pkg/sortedmap) = %{version}
Provides:       go(yunion.io/x/pkg/tristate) = %{version}
Provides:       go(yunion.io/x/pkg/util/reflectutils) = %{version}
Provides:       go(yunion.io/x/pkg/util/regutils) = %{version}
Provides:       go(yunion.io/x/pkg/util/signalutils) = %{version}
Provides:       go(yunion.io/x/pkg/util/timeutils) = %{version}
Provides:       go(yunion.io/x/pkg/utils) = %{version}

Requires:       go(github.com/pkg/errors)
Requires:       go(yunion.io/x/log)

%description
This package provides the base Cloudpods helpers used by jsonutils,
allowing jsonutils to build before the complete yunion.io/x/pkg module.

%prep -a
rm -rf vendor

%install
install -d %{buildroot}%{go_sys_gopath}/%{go_import_path}
cp -a --parents errors gotypes sortedmap tristate util/reflectutils util/regutils util/signalutils util/timeutils utils \
    %{buildroot}%{go_sys_gopath}/%{go_import_path}/

%files
%doc README.md
%license LICENSE
%dir %{go_sys_gopath}/%{go_import_path}
%dir %{go_sys_gopath}/%{go_import_path}/util
%{go_sys_gopath}/%{go_import_path}/errors
%{go_sys_gopath}/%{go_import_path}/gotypes
%{go_sys_gopath}/%{go_import_path}/sortedmap
%{go_sys_gopath}/%{go_import_path}/tristate
%{go_sys_gopath}/%{go_import_path}/util/reflectutils
%{go_sys_gopath}/%{go_import_path}/util/regutils
%{go_sys_gopath}/%{go_import_path}/util/signalutils
%{go_sys_gopath}/%{go_import_path}/util/timeutils
%{go_sys_gopath}/%{go_import_path}/utils

%changelog
%autochangelog
