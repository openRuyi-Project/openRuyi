# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           lsscsi
Version:        0.32
Release:        %autorelease
Summary:        The lsscsi command lists information about SCSI devices in Linux.
License:        GPL-2.0-or-later
URL:            http://sg.danny.cz/scsi/lsscsi.html
# VCS: No VCS link available
#!RemoteAsset
Source0:        http://sg.danny.cz/scsi/%{name}-%{version}.tgz
BuildSystem:    autotools

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake

%description
Using SCSI terminology, lsscsi lists SCSI logical units (or SCSI targets
when the '--transport' option is given). The default action is to produce
one line of output for each SCSI device currently attached to the system.
In version 0.30 of this utility, support was added to list NVMe namespaces
(under SCSI devices(LUs)) and NVMe controllers (under SCSI hosts).

%files
%doc ChangeLog INSTALL README CREDITS AUTHORS
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.8*

%changelog
%autochangelog
