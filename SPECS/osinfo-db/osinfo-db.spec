# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           osinfo-db
Version:        20250606
Release:        %autorelease
Summary:        Database of information about operating systems
License:        GPL-2.0-or-later
URL:            https://libosinfo.org/
VCS:            git:https://gitlab.com/libosinfo/osinfo-db
#!RemoteAsset
Source:         https://releases.pagure.org/libosinfo/osinfo-db-%{version}.tar.xz

BuildRequires:  osinfo-db-tools
BuildRequires:  intltool

Requires:       hwdata

%description
The osinfo database provides information about operating systems and
hypervisor platforms to facilitate the automated configuration and
provisioning of new virtual machines.

%install
osinfo-db-import --root %{buildroot} --dir %{_datadir}/osinfo %{SOURCE0}

%files
%dir %{_datadir}/osinfo/
%{_datadir}/osinfo/VERSION
%{_datadir}/osinfo/LICENSE
%{_datadir}/osinfo/datamap
%{_datadir}/osinfo/device
%{_datadir}/osinfo/os
%{_datadir}/osinfo/platform
%{_datadir}/osinfo/install-script
%{_datadir}/osinfo/schema

%changelog
%autochangelog
