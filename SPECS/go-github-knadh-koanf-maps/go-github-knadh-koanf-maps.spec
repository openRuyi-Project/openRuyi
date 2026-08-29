# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           maps
%define go_import_path  github.com/knadh/koanf/maps
%define go_source_subdir maps

Name:           go-github-knadh-koanf-maps
Version:        0.1.2
Release:        %autorelease
Summary:        Map utility module for koanf
License:        MIT
URL:            https://github.com/knadh/koanf
#!RemoteAsset:  sha256:2a5c4574eaee632a94e439999655f81b3346d157232b610eb2ebc49fd07ffe5a
Source0:        https://github.com/knadh/koanf/archive/refs/tags/maps/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# The upstream tag archive contains the whole koanf repository. The explicit
# %install/%check sections below enter %{go_source_subdir}; using
# BuildOption(prep): -n .../maps would copy the whole repository under the maps
# import path because the GitHub archive still contains the top-level directory. - HNO3Miracle

BuildRequires:  go
BuildRequires:  go(github.com/mitchellh/copystructure)
BuildRequires:  go(github.com/mitchellh/reflectwalk)
BuildRequires:  go-rpm-macros

Provides:       go(github.com/knadh/koanf/maps) = %{version}

Requires:       go(github.com/mitchellh/copystructure)
Requires:       go(github.com/mitchellh/reflectwalk)

%description
This package provides map utilities used by koanf and koanf provider modules.

%install
pushd %{go_source_subdir}
%buildsystem_golangmodules_install
popd

%check
pushd %{go_source_subdir}
%buildsystem_golangmodules_check
popd

%files
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
