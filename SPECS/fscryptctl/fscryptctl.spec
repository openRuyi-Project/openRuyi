# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           fscryptctl
Version:        1.3.0
Release:        %autorelease
Summary:        Low-level tool for handling Linux filesystem encryption
License:        Apache-2.0
URL:            https://github.com/google/fscryptctl
#!RemoteAsset
Source:         https://github.com/google/fscryptctl/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    autotools

Patch:          0001-disable-doc.patch

BuildOption(install):  PREFIX=%{_prefix}

BuildRequires:  gcc
BuildRequires:  make

%description
fscryptctl is a low-level tool written in C that handles raw keys and manages
policies for Linux filesystem encryption (fscrypt).

It is mainly intended for embedded systems or for testing. For a more
user-friendly, high-level tool, use fscrypt (written in Go) instead.

# No configure.
%conf

# Test setup requires root
%check

%files
%license LICENSE
%doc README.md NEWS.md CONTRIBUTING.md
%{_bindir}/fscryptctl

%changelog
%autochangelog
