# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name            goidentity
%define go_import_path   github.com/jcmturner/goidentity/v6

Name:           go-github-jcmturner-goidentity-v6
Version:        6.0.1
Release:        %autorelease
Summary:        Interface for authenticated identities in Go
License:        Apache-2.0
URL:            https://github.com/jcmturner/goidentity
#!RemoteAsset:  sha256:493e40431872340d8b7fdebb6ebb76442d0d52f362f4414bf28b69305c36fd81
Source0:        https://github.com/jcmturner/goidentity/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/hashicorp/go-uuid)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/jcmturner/goidentity/v6) = %{version}

Requires:       go(github.com/hashicorp/go-uuid)

%description
Goidentity defines a standard interface for authenticated identities and
their attributes.

%install
pushd v6
%buildsystem_golangmodules_install
popd

%check
pushd v6
%buildsystem_golangmodules_check
popd

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
