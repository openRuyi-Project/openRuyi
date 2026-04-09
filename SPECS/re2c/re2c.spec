# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Summary:        Lexer generator for C/C++
Name:           re2c
Version:        4.3
Release:        %autorelease
License:        LicenseRef-openRuyi-Public-Domain
URL:            https://re2c.org/
VCS:            git:https://github.com/skvadrik/re2c
#!RemoteAsset
Source:         https://github.com/skvadrik/re2c/releases/download/%{version}/re2c-%{version}.tar.xz
BuildSystem:    autotools

BuildRequires:  python3
BuildRequires:  gcc-c++

%description
re2c is a tool for writing very fast and very flexible scanners. Unlike any
other such tool, re2c focuses on generating high efficient code for regular
expression matching. As a result this allows a much broader range of use than
any traditional lexer offers. And Last but not least re2c generates warning
free code that is equal to hand-written code in terms of size, speed and
quality.

%files
%license LICENSE
%doc CHANGELOG README.md examples/ doc/*
%{_bindir}/re2c
%{_bindir}/re2d
%{_bindir}/re2go
%{_bindir}/re2hs
%{_bindir}/re2js
%{_bindir}/re2ocaml
%{_bindir}/re2py
%{_bindir}/re2rust
%{_bindir}/re2swift
%{_bindir}/re2v
%{_bindir}/re2zig
%{_datadir}/re2c/
%{_mandir}/man1/*.1.*

%changelog
%autochangelog
