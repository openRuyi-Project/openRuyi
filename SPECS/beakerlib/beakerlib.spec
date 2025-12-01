# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           beakerlib
Version:        1.31.6
Release:        %autorelease
Summary:        A shell-level integration testing library
License:        GPL-2.0-only
URL:            https://github.com/%{name}
#!RemoteAsset
Source0:        https://github.com/beakerlib/beakerlib/archive/refs/tags/1.31.6.tar.gz
Source1:        %{name}-tmpfiles.conf
BuildSystem:    autotools

BuildOption(build): build
BuildOption(install): DESTDIR=%{buildroot}/usr

BuildRequires:  perl
BuildRequires:  util-linux
BuildRequires:  make

Requires:       /bin/bash
Requires:       /bin/sh
Requires:       coreutils grep gzip iproute2 sed tar util-linux which
Requires:       /usr/bin/bc /usr/bin/time
Requires:       (wget or curl)
Requires:       nfs-utils
Recommends:     /usr/bin/perl python3-lxml /usr/bin/xmllint

%description
The BeakerLib project provides a library of shell functions to be used for
writing operating system level integration tests.

%package       vim-syntax
Summary: Files for syntax highlighting BeakerLib tests in VIM editor
Requires:      vim
BuildRequires: vim
BuildRequires: make

%description   vim-syntax
Files for syntax highlighting BeakerLib tests in VIM editor

# No configure
%conf

%install -a
mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 0644 %{SOURCE1} %{buildroot}%{_tmpfilesdir}/%{name}.conf

%files
%dir %{_datadir}/beakerlib
%dir %{_datadir}/beakerlib/xslt-templates
%{_datadir}/beakerlib/dictionary.vim
%{_datadir}/beakerlib/*.sh
%{_datadir}/beakerlib/xslt-templates/*
%{_bindir}/beakerlib-*
%{_mandir}/man1/beakerlib*1*
%doc %{_docdir}/beakerlib
%config %{_tmpfilesdir}/beakerlib.conf

%files vim-syntax
%{_datadir}/vim/vimfiles/after/ftdetect/beakerlib.vim
%{_datadir}/vim/vimfiles/after/syntax/beakerlib.vim

%changelog
%{?autochangelog}
