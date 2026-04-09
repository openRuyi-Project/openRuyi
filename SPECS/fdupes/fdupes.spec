# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           fdupes
Version:        2.4.0
Release:        %autorelease
Summary:        Tool to identify or delete duplicate files
License:        MIT
URL:            https://github.com/adrianlopezroche/fdupes
#!RemoteAsset
Source0:        https://github.com/adrianlopezroche/fdupes/releases/download/v%{version}/fdupes-%{version}.tar.gz
Source1:        macros.fdupes
Source2:        fdupes_wrapper.cpp
BuildSystem:    autotools

BuildOption(conf):  --without-ncurses
BuildOption(conf):  --without-sqlite

BuildRequires:  gcc-c++

%description
FDUPES is a program for identifying or deleting duplicate files
residing within specified directories.

%build -a
g++ -O2 %{SOURCE2} -o fdupes_wrapper

%install -a
install -D -m644 %{SOURCE1} %{buildroot}%{_rpmmacrodir}/macros.%{name}
install -D -m755 fdupes_wrapper  %{buildroot}%{_prefix}/lib/rpm/fdupes_wrapper

%files
%{_bindir}/fdupes
%{_mandir}/man1/fdupes.1*
%{_rpmmacrodir}/macros.%{name}
%{_prefix}/lib/rpm/fdupes_wrapper

%changelog
%autochangelog
