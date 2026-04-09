# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: jchzhou <zhoujiacheng@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           hwdata
Version:        0.398
Release:        %autorelease
Summary:        Hardware identification and configuration data
License:        GPL-2.0-or-later
URL:            https://github.com/vcrhonek/hwdata
#!RemoteAsset
Source0:        https://github.com/vcrhonek/hwdata/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    autotools

BuildOption(install):  libdir=%{_libdir}

BuildRequires:  make
BuildRequires:  pciutils
# for tests fix.
BuildRequires:  python3
BuildRequires:  python3-rpm-macros

%description
hwdata contains various hardware identification and configuration data,
such as the pci.ids and usb.ids databases.

%check -p
%py3_shebang_fix .

%files
%license COPYING
%doc LICENSE
%dir %{_datadir}/hwdata
%{_prefix}/lib/modprobe.d/dist-blacklist.conf
%{_datadir}/hwdata/*
%{_datadir}/pkgconfig/hwdata.pc

%changelog
%autochangelog
