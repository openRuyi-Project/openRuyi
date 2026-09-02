# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           kobject
%define go_import_path  github.com/mdlayher/kobject
%define commit_id       19ca17470d7db4a13d1ea097667c16740988b179

Name:           go-github-mdlayher-kobject
Version:        0+git20260819.19ca174
Release:        %autorelease
Summary:        Linux kobject userspace event access for Go
License:        MIT
URL:            https://github.com/mdlayher/kobject
#!RemoteAsset:  sha256:8224cb9ade5646fe511462c1d48a171bf7cb2f431baa280f66e1983631c1f22e
Source0:        https://github.com/mdlayher/kobject/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules
BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/mdlayher/netlink)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/mdlayher/netlink)
Requires:       go(golang.org/x/sys)

%description
Kobject provides access to Linux kobject userspace events such as device and
network interface additions and removals.

%files
%doc README.md
%license LICENSE.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
