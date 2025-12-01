# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           virt-what
Version:        1.27
Release:        %autorelease
Summary:        Detect if running in a virtual machine
License:        GPL-2.0-or-later
#!RemoteAsset
URL:            https://people.redhat.com/~rjones/%{name}/
#!RemoteAsset
Source:         https://people.redhat.com/~rjones/%{name}/files/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  gcc util-linux
BuildRequires:  perl
Requires:       dmidecode util-linux which

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
%{?autochangelog}
