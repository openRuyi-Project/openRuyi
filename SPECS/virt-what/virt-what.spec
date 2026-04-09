# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           virt-what
Version:        1.27
Release:        %autorelease
Summary:        Detect if running in a virtual machine
License:        GPL-2.0-or-later
URL:            https://people.redhat.com/~rjones/virt-what/
VCS:            git:git://git.annexia.org/virt-what.git
#!RemoteAsset
Source:         https://people.redhat.com/~rjones/%{name}/files/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  gcc
BuildRequires:  util-linux
BuildRequires:  perl

Requires:       dmidecode
Requires:       util-linux
Requires:       which

%description
virt-what is a shell script which can be used to detect if the program
is running in a virtual machine.

%files
%doc README
%license COPYING
%{_sbindir}/*
%{_libexecdir}/virt-what-cpuid-helper
%{_mandir}/man1/*

%changelog
%autochangelog
