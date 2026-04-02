# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global _test_target test

Name:           multipath-tools
Version:        0.11.1
Release:        %autorelease
Summary:        Tools to manage multipath devices using device-mapper
License:        GPL-2.0-only AND GPL-3.0-or-later
URL:            https://github.com/opensvc/multipath-tools
#!RemoteAsset
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    autotools

# From https://github.com/opensvc/multipath-tools/commit/9f611e2f10a4456477b6447641eea041ecee1019
Patch0:         multipath-tools-fix-c23-errors-with-strchr.patch

BuildOption(conf):  LIB=%{_lib}
BuildOption(install):  bindir=%{_sbindir}
BuildOption(install):  syslibdir=%{_libdir}
BuildOption(install):  usrlibdir=%{_libdir}
BuildOption(install):  plugindir=%{_libmpathdir}
BuildOption(install):  mandir=%{_mandir}
BuildOption(install):  unitdir=%{_unitdir}
BuildOption(install):  includedir=%{_includedir}
BuildOption(install):  pkgconfigdir=%{_pkgconfdir}
BuildOption(install):  tmpfilesdir=%{_tmpfilesdir}

BuildRequires:  libaio-devel
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(devmapper)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(liburcu)
BuildRequires:  pkgconfig(mount)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(cmocka)

Requires:       device-mapper >= 1.2.78
Requires:       kpartx

%description
multipath-tools provides tools to manage multipath devices by
instructing the device-mapper multipath kernel module what to do.
The tools are :
* multipath - Scan the system for multipath devices and assemble them.
* multipathd - Detects when paths fail and execs multipath to update things.

%package        libs
Summary:        The multipath-tools modules and shared library
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-2.0-or-later

%description    libs
The multipath-tools-libs provides the path checker
and prioritizer modules. It also contains the libmpathpersist and
libmpathcmd shared libraries, as well as multipath's internal library,
libmultipath.

%package        devel
Summary:        Development libraries and headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
This package contains the files need to develop applications that use
device-mapper-multipath's lbmpathpersist and libmpathcmd libraries.

%package     -n kpartx
Summary: Partition device manager for device-mapper devices

%description -n kpartx
kpartx manages partition creation and removal for device-mapper devices.

%package     -n libdmmp
Summary:        device-mapper-multipath C API library
License:        GPL-3.0-or-later
Requires:       json-c
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-libs = %{version}-%{release}

%description -n libdmmp
This package contains the shared library for the device-mapper-multipath
C API library.

%package     -n libdmmp-devel
Summary:        device-mapper-multipath C API library headers
Requires:       pkgconfig
Requires:       libdmmp%{?_isa} = %{version}-%{release}

%description -n libdmmp-devel
This package contains the files needed to develop applications that use
device-mapper-multipath's libdmmp C API library

%conf
# No conf

%build -p
%define _libdir /usr/%{_lib}
%define _libmpathdir %{_libdir}/multipath
%define _pkgconfdir %{_libdir}/pkgconfig

%install -a
# tree fix up
install -d %{buildroot}/etc/multipath
rm -rf %{buildroot}/%{_initrddir}

%post
%tmpfiles_create %{_tmpfilesdir}/multipath.conf
%systemd_post multipathd.service

%preun
%systemd_preun multipathd.service

%postun
if [ $1 -ge 1 ] ; then
       multipathd forcequeueing daemon > /dev/null 2>&1 || :
fi
%systemd_postun_with_restart multipathd.service

%files
%license LICENSES/GPL-2.0 LICENSES/LGPL-2.0 LICENSES/GPL-3.0
%{_sbindir}/multipath
%{_sbindir}/multipathd
%{_sbindir}/multipathc
%{_sbindir}/mpathpersist
%{_unitdir}/multipathd.service
%{_unitdir}/multipathd.socket
%{_mandir}/man5/multipath.conf.5*
%{_mandir}/man8/multipath.8*
%{_mandir}/man8/multipathd.8*
%{_mandir}/man8/multipathc.8*
%{_mandir}/man8/mpathpersist.8*
%config /usr/lib/udev/rules.d/56-multipath.rules
%config /usr/lib/udev/rules.d/11-dm-mpath.rules
%config /usr/lib/udev/rules.d/99-z-dm-mpath-late.rules
%dir %{_modulesloaddir}
%{_tmpfilesdir}/multipath.conf
%doc README.md
%dir /etc/multipath

%files libs
%license LICENSES/GPL-2.0 LICENSES/LGPL-2.0 LICENSES/LGPL-2.1
%doc README.md
%{_libdir}/libmultipath.so
%{_libdir}/libmultipath.so.*
%{_libdir}/libmpathutil.so
%{_libdir}/libmpathutil.so.*
%{_libdir}/libmpathpersist.so.*
%{_libdir}/libmpathcmd.so.*
%{_libdir}/libmpathvalid.so.*
%dir %{_libmpathdir}
%{_libmpathdir}/*

%files devel
%doc README.md
%{_libdir}/libmpathpersist.so
%{_libdir}/libmpathcmd.so
%{_libdir}/libmpathvalid.so
%{_includedir}/mpath_cmd.h
%{_includedir}/mpath_persist.h
%{_includedir}/mpath_valid.h
%{_mandir}/man3/mpath_persistent_reserve_in.3*
%{_mandir}/man3/mpath_persistent_reserve_out.3*

%files -n kpartx
%license LICENSES/GPL-2.0
%doc README.md
%{_sbindir}/kpartx
/usr/lib/udev/kpartx_id
%{_mandir}/man8/kpartx.8*
%config %{_udevrulesdir}/11-dm-parts.rules
%config %{_udevrulesdir}/66-kpartx.rules
%config %{_udevrulesdir}/68-del-part-nodes.rules

%files -n libdmmp
%license LICENSES/GPL-3.0
%doc README.md
%{_libdir}/libdmmp.so.*

%files -n libdmmp-devel
%doc README.md
%{_libdir}/libdmmp.so
%dir %{_includedir}/libdmmp
%{_includedir}/libdmmp/*
%{_mandir}/man3/dmmp_*
%{_mandir}/man3/libdmmp.h.3*
%{_pkgconfdir}/libdmmp.pc

%changelog
%{?autochangelog}
