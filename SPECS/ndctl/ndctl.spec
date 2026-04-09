# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond doc 0
%bcond trace 0

Name:           ndctl
Version:        83
Release:        %autorelease
Summary:        Manage "libnvdimm" subsystem devices (Non-volatile Memory)
License:        GPL-2.0-only AND LGPL-2.1-only AND CC0-1.0 AND MIT
URL:            https://github.com/pmem/ndctl
#!RemoteAsset
Source0:        https://github.com/pmem/ndctl/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    meson

BuildOption(conf):  -Dversion-tag=%{version}
BuildOption(conf):  -Ddocs=disabled
BuildOption(conf):  -Dsystemd=enabled
%if %{with doc}
BuildOption(conf):  -Dasciidoctor=enabled
%else
BuildOption(conf):  -Dasciidoctor=disabled
%endif
%if %{with trace}
BuildOption(conf):  -Dlibtracefs=enabled
%else
BuildOption(conf):  -Dlibtracefs=disabled
%endif

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libkmod)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(libkeyutils)
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(iniparser)
%if %{with doc}
BuildRequires:  rubygem-asciidoctor
BuildRequires:  xmlto
%endif
%if %{with trace}
BuildRequires:  pkgconfig(libtraceevent)
BuildRequires:  pkgconfig(libtracefs)
%endif

%description
Utility library for managing the "libnvdimm" subsystem.

%package        devel
Summary:        Development files for libndctl,libdaxctl and libcxl.
License:        LGPL-2.1-only
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for libndctl,libdaxctl and libcx.

%install -a
%global bashcompdir %(pkg-config --variable=completionsdir bash-completion)

%files
%doc README.md
%license LICENSES/preferred/GPL-2.0 LICENSES/other/MIT LICENSES/other/CC0-1.0
%{_bindir}/ndctl
%{bashcompdir}/ndctl
%{_unitdir}/ndctl-monitor.service
%dir %{_sysconfdir}/ndctl
%dir %{_sysconfdir}/ndctl/keys
%{_sysconfdir}/ndctl/keys/keys.readme
%{_sysconfdir}/modprobe.d/nvdimm-security.conf
%dir %{_sysconfdir}/ndctl.conf.d
%config(noreplace) %{_sysconfdir}/ndctl.conf.d/monitor.conf
%config(noreplace) %{_sysconfdir}/ndctl.conf.d/ndctl.conf
%{_bindir}/daxctl
%{_datadir}/daxctl
%{bashcompdir}/daxctl
%{_unitdir}/daxdev-reconfigure@.service
%config %{_udevrulesdir}/90-daxctl-device.rules
%dir %{_sysconfdir}/daxctl.conf.d/
%config(noreplace) %{_sysconfdir}/daxctl.conf.d/daxctl.example.conf
%if %{with doc}
%{_mandir}/man1/daxctl*
%{_mandir}/man1/cxl*
%{_mandir}/man1/ndctl*
%endif
%{_bindir}/cxl
%{bashcompdir}/cxl
%{_unitdir}/cxl-monitor.service
# ndctl-libs
%{_libdir}/libndctl.so.*
# daxctl-libs
%{_libdir}/libdaxctl.so.*
# cxl-libs
%{_libdir}/libcxl.so.*

%files devel
%license LICENSES/preferred/LGPL-2.1
%{_includedir}/ndctl/
%{_libdir}/libndctl.so
%{_libdir}/pkgconfig/libndctl.pc
%{_includedir}/daxctl/
%{_libdir}/libdaxctl.so
%{_libdir}/pkgconfig/libdaxctl.pc
%{_includedir}/cxl/
%{_libdir}/libcxl.so
%{_libdir}/pkgconfig/libcxl.pc
%if %{with doc}
%{_mandir}/man3/cxl*
%{_mandir}/man3/libcxl.3*
%endif

%changelog
%autochangelog
