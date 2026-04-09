# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           ipset
Version:        7.24
Release:        %autorelease
Summary:        Manage Linux IP sets
License:        GPL-2.0-only
URL:            http://ipset.netfilter.org/
VCS:            git:https://git.netfilter.org/ipset
#!RemoteAsset
Source0:        %{url}/ipset-%{version}.tar.bz2
Source1:        ipset.service
BuildSystem:    autotools

BuildOption(conf):  --enable-static=no
BuildOption(conf):  --with-kmod=no

BuildRequires:  make
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  pkgconfig(libmnl)

%description
IP sets are a framework inside the Linux kernel since version 2.4.x, which can
be administered by the ipset utility. Depending on the type, currently an IP
set may store IP addresses, (TCP/UDP) port numbers or IP addresses with MAC
addresses in a way, which ensures lightning speed when matching an entry
against a set.

If you want to:
 - store multiple IP addresses or port numbers and match against the collection
   by iptables at one swoop;
 - dynamically update iptables rules against IP addresses or ports without
   performance penalty;
 - express complex IP address and ports based rulesets with one single iptables
   rule and benefit from the speed of IP sets
then ipset may be the proper tool for you.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} == %{version}-%{release}
Requires:       linux-headers

%description    devel
This package contains the files required to develop software using the %{name}
libraries.

%conf -p
./autogen.sh

%conf -a
# We don't build the bundled kernel module
rm -rf kernel
# Prevent libtool from defining rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%install -a
# install systemd unit file
install -d -m 755 %{buildroot}%{_unitdir}
install -c -m 644 %{SOURCE1} %{buildroot}%{_unitdir}

%post
%systemd_post ipset.service

%preun
%systemd_preun ipset.service

%postun
%systemd_postun_with_restart ipset.service

%files
%doc ChangeLog
%license COPYING
%{_mandir}/man8/ipset*.8.*
%{_libdir}/libipset.so.13*
%{_sbindir}/ipset
%{_sbindir}/ipset-translate
%{_unitdir}/ipset.service

%files devel
%{_includedir}/libipset
%{_libdir}/libipset.so
%{_libdir}/pkgconfig/libipset.pc
%{_mandir}/man3/libipset.3.*

%changelog
%autochangelog
