# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           base64x
%define go_import_path  github.com/chenzhuoyu/base64x

Name:           go-github-chenzhuoyu-base64x
Version:        0+git20261029.296ad89
Release:        %autorelease
Summary:        High-performance replacement for Go encoding/base64
License:        Apache-2.0
URL:            https://github.com/chenzhuoyu/base64x
#!RemoteAsset:  sha256:26664e91ef75748f41f2a0651d182d9900f404facb006f8b14a221de57b4a8d6
Source0:        https://github.com/chenzhuoyu/base64x/archive/296ad89f973d.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n base64x-296ad89f973dd706aa9661b49f4443b95c5d95af

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/bytedance/sonic)
BuildRequires:  go(github.com/bytedance/sonic/loader)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/klauspost/cpuid/v2)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/bytedance/sonic)
Requires:       go(github.com/bytedance/sonic/loader)
Requires:       go(github.com/klauspost/cpuid/v2)

%description
base64x is a high-performance drop-in replacement for Go's
encoding/base64 package. It uses Sonic runtime loading on supported
architectures and retains the complete upstream test and tool sources.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
