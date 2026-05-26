# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           confmap
%define go_import_path  github.com/knadh/koanf/providers/confmap
%define go_source_subdir providers/confmap

Name:           go-github-knadh-koanf-providers-confmap
Version:        1.0.0
Release:        %autorelease
Summary:        Confmap provider module for koanf
License:        MIT
URL:            https://github.com/knadh/koanf
#!RemoteAsset:  sha256:96f291f4f4d1eed2eb8cdf3c74e469bf1d318f2f86822e802267726c5611b1a1
Source0:        https://github.com/knadh/koanf/archive/refs/tags/providers/confmap/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# The upstream tag archive contains the whole koanf repository. The explicit
# %install/%check sections below enter %{go_source_subdir}; using
# BuildOption(prep): -n .../providers/confmap would copy the whole repository
# under the provider import path because the GitHub archive still contains the
# top-level directory. - HNO3Miracle

BuildRequires:  go
BuildRequires:  go(github.com/knadh/koanf/maps)
BuildRequires:  go(github.com/mitchellh/copystructure)
BuildRequires:  go(github.com/mitchellh/reflectwalk)
BuildRequires:  go-rpm-macros

Provides:       go(github.com/knadh/koanf/providers/confmap) = %{version}

Requires:       go(github.com/knadh/koanf/maps)
Requires:       go(github.com/mitchellh/copystructure)
Requires:       go(github.com/mitchellh/reflectwalk)

%description
This package provides the confmap provider module for koanf.

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
