# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           haveged
Version:        1.9.20
Release:        %autorelease
Summary:        A Linux entropy source using the HAVEGE algorithm
License:        GPL-3.0-or-later
URL:            https://github.com/jirka-h/haveged
#!RemoteAsset:  sha256:215d64f98e84ad30795dcf3b58a10c8a821589f8967057c570da0b5e83de2c52
Source0:        https://github.com/jirka-h/haveged/archive/refs/tags/v%{version}.tar.gz
Source1:        haveged.service
Source2:        90-haveged.rules
Source3:        haveged-dracut.module
BuildSystem:    autotools

BuildOption(conf):  --disable-enttest
BuildOption(conf):  --enable-nistest
BuildOption(conf):  --disable-static

BuildRequires:  make
BuildRequires:  automake
BuildRequires:  systemd-rpm-macros

Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

%description
Haveged is a user space entropy daemon which is not dependent upon the
standard mechanisms for harvesting randomness for the system entropy pool.
It uses the HAVEGE algorithm to maintain a pool of random bytes.

%package        devel
Summary:        Headers and shared development libraries for HAVEGE algorithm
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers and shared object symbolic links for the HAVEGE algorithm.

%install -a
rm -f %{buildroot}%{_libdir}/libhavege.*a

install -Dpm 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -Dpm 0644 %{SOURCE2} %{buildroot}%{_udevrulesdir}/90-%{name}.rules
install -Dpm 0755 %{SOURCE3} %{buildroot}%{_prefix}/lib/dracut/modules.d/98%{name}/module-setup.sh

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license COPYING
%{_sbindir}/haveged
%{_mandir}/man8/haveged.8*
%{_unitdir}/haveged.service
%{_udevrulesdir}/90-haveged.rules
%dir %{_prefix}/lib/dracut
%dir %{_prefix}/lib/dracut/modules.d
%dir %{_prefix}/lib/dracut/modules.d/98haveged
%{_prefix}/lib/dracut/modules.d/98haveged/module-setup.sh
%{_libdir}/*.so.*

%files devel
%license COPYING
%{_mandir}/man3/libhavege.3*
%dir %{_includedir}/haveged
%{_includedir}/haveged/havege.h
%doc contrib/build/havege_sample.c
%{_libdir}/*.so

%changelog
%autochangelog
