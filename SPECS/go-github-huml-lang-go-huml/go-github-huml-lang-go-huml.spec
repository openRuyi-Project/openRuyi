# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-huml
%define go_import_path  github.com/huml-lang/go-huml
%define tests_commit    0c3b64965f538d6ca92243af0d091c5798aaa92e

Name:           go-github-huml-lang-go-huml
Version:        0.3.0
Release:        %autorelease
Summary:        Parser and encoder for Human-oriented Markup Language
License:        MIT
URL:            https://github.com/huml-lang/go-huml
#!RemoteAsset:  sha256:c8d97d3d336f1c1f357b659a7e698ba35921495832d83e65df5dab4f7118131e
Source0:        https://github.com/huml-lang/go-huml/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
#!RemoteAsset:  sha256:82ab05f9710deb4526f8ddbc42c4e7ad4f2407269cf2f748557f4caa87c00804
Source1:        https://github.com/huml-lang/tests/archive/%{tests_commit}.tar.gz#/%{_name}-tests-%{tests_commit}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
Go-huml parses, encodes, and decodes documents written in Human-oriented
Markup Language.

%prep
%autosetup -n %{_name}-%{version} -a 1
# The source archive contains an empty tests/ directory; replace it with the
# fixture archive instead of nesting the extracted directory below it.
rm -rf tests
mv tests-%{tests_commit} tests

%install -a
cp -a tests %{buildroot}%{go_sys_gopath}/%{go_import_path}/

%check
%go_common
%go_prep
cp -a tests %{_builddir}/go/src/%{go_import_path}/
cd %{_builddir}/go/src/%{go_import_path}
%__go test -v %{go_import_path}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
