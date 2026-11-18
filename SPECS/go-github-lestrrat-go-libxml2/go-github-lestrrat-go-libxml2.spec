# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           libxml2
%define go_import_path  github.com/lestrrat-go/libxml2
%define commit_id       3f0f7bd60b63aadec79b0851b9adaa50d14782af

Name:           go-github-lestrrat-go-libxml2
Version:        0+git20261022.3f0f7bd
Release:        %autorelease
Summary:        Go bindings for libxml2 parsing, DOM, XPath, and XML schemas
License:        MIT
URL:            https://github.com/lestrrat-go/libxml2
#!RemoteAsset:  sha256:aef0431f3237d4dd21a489813d61240a8ca8cd191ae0c3f477fc8b46b9a7c018
Source0:        https://github.com/lestrrat-go/libxml2/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Bridge libxml2's xmlNode pointer typedef for current CGO type checking.
# https://github.com/atulpatildbz/libxml2/commit/d06374c0f56fe2f3e7ff6dacc46d0d376a6c88bd
Patch2000:      2000-fix-xmlParseInNodeContext-cgo-types.patch

BuildOption(prep):  -n %{_name}-%{commit_id} -p1
# Upstream's ExampleXML and ExampleHTML do not name exported identifiers.
# Current vet rejects those names; keep the full test suite enabled.
BuildOption(check):  -vet=off

BuildRequires:  gcc
BuildRequires:  go >= 1.21
BuildRequires:  go-rpm-macros
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/pkg/errors)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(gopkg.in/xmlpath.v1)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go(launchpad.net/gocheck)
BuildRequires:  go(launchpad.net/xmlpath)

Provides:       go(%{go_import_path}) = %{version}
Provides:       go(%{go_import_path}/clib) = %{version}
Provides:       go(%{go_import_path}/dom) = %{version}
Provides:       go(%{go_import_path}/internal/debug) = %{version}
Provides:       go(%{go_import_path}/internal/option) = %{version}
Provides:       go(%{go_import_path}/parser) = %{version}
Provides:       go(%{go_import_path}/types) = %{version}
Provides:       go(%{go_import_path}/xpath) = %{version}
Provides:       go(%{go_import_path}/xsd) = %{version}

Requires:       pkgconfig(libxml-2.0)
Requires:       go(github.com/pkg/errors)

%description
Go bindings for the system libxml2 library provide XML and HTML parsing,
DOM manipulation, XPath evaluation, and XML Schema validation. This package
includes the complete upstream source tree, examples, tests, and fixtures.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
