# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           loader
%define go_import_path  github.com/bytedance/sonic/loader
%define go_source_subdir loader

Name:           go-github-bytedance-sonic-loader
Version:        0.5.1
Release:        %autorelease
Summary:        Runtime loader for dynamically generated Go functions
License:        Apache-2.0
URL:            https://github.com/bytedance/sonic
#!RemoteAsset:  sha256:77f6b5853144d0a242601333242264e729d58559072a8664b1dcc476e6a1bac8
Source0:        https://github.com/bytedance/sonic/archive/refs/tags/loader/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n sonic-loader-v%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/bytedance/sonic/loader) = %{version}

%description
sonic/loader loads machine code and function metadata into the Go runtime as
callable functions. It is intended for runtime code generation and is used by
the Sonic JSON library.

%install
pushd %{go_source_subdir}
%buildsystem_golangmodules_install
popd

%check
# sonic/loader implements its runtime ABI only for amd64
%ifarch x86_64
pushd %{go_source_subdir}
%buildsystem_golangmodules_check
popd
%endif

%files
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
