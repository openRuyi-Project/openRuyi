# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           beakerlib
Version:        1.33.3
Release:        %autorelease
Summary:        A shell-level integration testing library
License:        GPL-2.0-only
URL:            https://github.com/beakerlib/beakerlib
#!RemoteAsset:  sha256:87a054194ddd2e073d50c15b0c4f7cf1373b1a5a82e78d9a8f16f13ade7ee00e
Source0:        https://github.com/beakerlib/beakerlib/archive/refs/tags/%{version}.tar.gz
Source1:        beakerlib.tmpfiles
BuildSystem:    autotools

BuildOption(build):  build
BuildOption(install):  DESTDIR=%{buildroot}/usr

BuildRequires:  perl
BuildRequires:  util-linux
BuildRequires:  make

Requires:       bash
Requires:       coreutils
Requires:       grep
Requires:       gzip
Requires:       iproute2
Requires:       sed
Requires:       tar
Requires:       util-linux
Requires:       which
Requires:       bc
Requires:       time
Requires:       (wget or curl)
Requires:       nfs-kernel-server

Recommends:     perl
Recommends:     python3dist(lxml)
Recommends:     libxml2

%description
The BeakerLib project provides a library of shell functions to be used for
writing operating system level integration tests.

%package        vim-syntax
Summary:        Files for syntax highlighting BeakerLib tests in VIM editor
BuildRequires:  vim
BuildRequires:  make
Requires:       vim

%description    vim-syntax
Files for syntax highlighting BeakerLib tests in VIM editor

# No configure
%conf

%install -a
mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 0644 %{SOURCE1} %{buildroot}%{_tmpfilesdir}/%{name}.conf

# No check
%check

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
%autochangelog
