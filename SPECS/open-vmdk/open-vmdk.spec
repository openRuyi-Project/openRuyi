# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           open-vmdk
Version:        0.3.12
Release:        %autorelease
Summary:        Tools to create OVA files from raw disk images
License:        Apache-2.0
URL:            https://github.com/vmware/open-vmdk
#!RemoteAsset
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(zlib)

Requires:       coreutils
Requires:       grep
Requires:       python3dist(pyyaml)
Requires:       python3dist(lxml)
Requires:       sed
Requires:       tar
Requires:       util-linux

%description
Open VMDK is an assistant tool for creating Open Virtual Appliance (OVA).

# No Configure.
%conf

%install -a
install -m0644 templates/*.ovf %{buildroot}%{_datadir}/%{name}

# No check.
%check

%files
%{_bindir}/mkova.sh
%{_bindir}/ova-compose
%{_bindir}/ovfenv
%{_bindir}/vmdk-convert
%{_datadir}/%{name}
%config(noreplace) %{_sysconfdir}/open-vmdk.conf

%changelog
%autochangelog
