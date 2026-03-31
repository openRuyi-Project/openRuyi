# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jingkun Zheng <zhengjingkun@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           pesign
Version:        116
Release:        %autorelease
Summary:        Signing utility for UEFI binaries
License:        GPL-2.0-only
URL:            https://github.com/rhboot/pesign
#!RemoteAsset
Source0:        https://github.com/rhboot/pesign/releases/download/%{version}/pesign-%{version}.tar.bz2
Source1:        pesign.py
Source2:        pesign.sysusers
BuildSystem:    autotools

Patch0:         0001-cms_common-Fixed-Segmentation-fault.patch
Patch1:         0002-Fix-reversed-calloc-arguments.patch
Patch2:         0003-Work-around-OpenSC-changing-token-names-on-fedora-bu.patch
Patch3:         0004-cms_common-skip-authentication-on-the-Friendly-slot.patch

BuildOption(build):  PREFIX=%{_prefix}
BuildOption(build):  LIBDIR=%{_libdir}
BuildOption(build):  LDFLAGS="${LDFLAGS} -pie -lnssutil3"
BuildOption(install):  PREFIX=%{_prefix}
BuildOption(install):  LIBDIR=%{_libdir}
BuildOption(install):  INSTALLROOT=%{buildroot}
BuildOption(install):  install_systemd

BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(efivar)
BuildRequires:  mandoc
BuildRequires:  pkgconfig(nspr)
BuildRequires:  pkgconfig(nss-util)
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(popt)
BuildRequires:  python3
BuildRequires:  libuuid
BuildRequires:  util-linux-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(python3)

Requires:       nss

%description
This package contains the pesign utility for signing UEFI binaries as
well as other associated tools.

# No configure
%conf

# No tests
%check

%install -a
mkdir -p %{buildroot}%{_sysconfdir}/pki/pesign/
rm -rf %{buildroot}/boot %{buildroot}/usr/include
rm -rf %{buildroot}%{_libdir}/libdpe*

mkdir -p %{buildroot}%{_rpmmacrodir}
mv %{buildroot}%{_sysconfdir}/rpm/macros.pesign %{buildroot}%{_rpmmacrodir}/
rmdir %{buildroot}%{_sysconfdir}/rpm
rm -f %{buildroot}/usr/share/doc/pesign-%{version}/COPYING

install -d -m 0755 %{buildroot}%{python3_sitelib}/mockbuild/plugins/
install -m 0755 %{SOURCE1} %{buildroot}%{python3_sitelib}/mockbuild/plugins/

install -m0644 -D %{SOURCE2} %{buildroot}%{_sysusersdir}/pesign.conf

%pre
%sysusers_create_package %{name} %{SOURCE2}

%post
%systemd_post pesign.service

%preun
%systemd_preun pesign.service

%postun
%systemd_postun_with_restart pesign.service

%files
%license COPYING
%doc README.md TODO COPYING
%{_bindir}/authvar
%{_bindir}/efikeygen
%{_bindir}/pesigcheck
%{_bindir}/pesign
%{_bindir}/pesign-client
%{_bindir}/pesum
%dir %{_libexecdir}/pesign/
%{_libexecdir}/pesign/pesign*
%config(noreplace)/%{_sysconfdir}/pesign/*
%{_sysconfdir}/popt.d/pesign.popt
%{_mandir}/man*/*
%dir %attr(0770, pesign, pesign) %{_rundir}/%{name}
%ghost %attr(0660, -, -) %{_rundir}/%{name}/socket
%ghost %attr(0660, -, -) %{_rundir}/%{name}/pesign.pid
%{_tmpfilesdir}/pesign.conf
%{_unitdir}/pesign.service
%{_sysusersdir}/pesign.conf
%{_rpmmacrodir}/macros.pesign
%{python3_sitelib}/mockbuild/plugins/pesign.*

%changelog
%{?autochangelog}
