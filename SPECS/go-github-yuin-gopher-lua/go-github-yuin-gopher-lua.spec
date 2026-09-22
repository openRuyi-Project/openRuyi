# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gopher-lua
%define go_import_path  github.com/yuin/gopher-lua

Name:           go-github-yuin-gopher-lua
Version:        0+git20210529.f4c35e4
Release:        %autorelease
Summary:        GopherLua: VM and compiler for Lua in Go
License:        MIT
URL:            https://github.com/yuin/gopher-lua
VCS:            git:https://github.com/yuin/gopher-lua.git
#!RemoteAsset:  sha256:adb4368b10c7160e41b44ec855354ec890cd3a6b712e7dafa2c6b84d10f98119
Source0:        https://github.com/yuin/gopher-lua/archive/f4c35e4016d9.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n gopher-lua-f4c35e4016d9d8580b007ebaeb68ecd8e0b09f1c
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/chzyer/readline)

Provides:       go(github.com/yuin/gopher-lua) = %{version}

Requires:       go(github.com/chzyer/readline)

%description
This package provides the github.com/yuin/gopher-lua Go module source.

%files
%doc README.rst
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
