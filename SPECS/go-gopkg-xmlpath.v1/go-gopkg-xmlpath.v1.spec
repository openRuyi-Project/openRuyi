# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           xmlpath
%define go_import_path  gopkg.in/xmlpath.v1
%define commit_id       a146725ea6e7e357ca683ef3e02e8a403742b9c0

Name:           go-gopkg-xmlpath.v1
Version:        0+git20261023.a146725
Release:        %autorelease
Summary:        XPath evaluation for Go XML documents
# LICENSE grants an additional exception for statically and dynamically linked applications.
License:        LicenseRef-xmlpath
URL:            https://github.com/go-xmlpath/xmlpath
#!RemoteAsset:  sha256:efe3184973778ef35dfbc9f9b2d00ce5957a1092fd2ee1c16a5d9f43d8349901
Source0:        https://github.com/go-xmlpath/xmlpath/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(launchpad.net/gocheck)

Provides:       go(%{go_import_path}) = %{version}
# This snapshot's own tests still import the historical Launchpad path.
Provides:       go(launchpad.net/xmlpath) = %{version}

%description
Xmlpath evaluates a subset of XPath expressions against parsed XML and HTML
documents. The complete v1 source snapshot includes its tests and the
historical launchpad.net/xmlpath import path used by those tests.

%install -a
# Both documented import paths use the same complete upstream snapshot.
install -d %{buildroot}%{go_sys_gopath}/launchpad.net
ln -s ../%{go_import_path} %{buildroot}%{go_sys_gopath}/launchpad.net/xmlpath

%check
# The default checker resets GOPATH; use the installed tree so both import
# paths resolve to the same snapshot while running both complete suites.
%go_common
export GOPATH="%{buildroot}%{go_sys_gopath}/..:${GOPATH}"
%__go test %{go_test_flags_default} %{go_import_path} launchpad.net/xmlpath

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}
%dir %{go_sys_gopath}/launchpad.net
%{go_sys_gopath}/launchpad.net/xmlpath

%changelog
%autochangelog
