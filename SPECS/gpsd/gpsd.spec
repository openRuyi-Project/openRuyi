# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           gpsd
Version:        3.27.5
Release:        %autorelease
Summary:        Service daemon for mediating access to a GPS
License:        BSD-2-Clause
URL:            https://gitlab.com/gpsd/gpsd
#!RemoteAsset:  sha256:409873f5048462ef1ac413a51ab35caa8b50b31be62b3347bee1cc2994e7c649
Source0:        https://download-mirror.savannah.gnu.org/releases/gpsd/gpsd-%{version}.tar.gz
Source1:        gpsd.sysconfig

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(scons)
BuildRequires:  python3dist(pyserial)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  desktop-file-utils
BuildRequires:  systemd-rpm-macros
BuildRequires:  xmlto
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Widgets)

Requires:       udev
%{?systemd_requires}

%description
gpsd is a service daemon that mediates access to a GPS sensor.

%package        devel
Summary:        Development files for the gpsd library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for gpsd library.

%package        qt6-devel
Summary:        Development files for the C++/Qt6 bindings
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    qt6-devel
Development files for Qt bindings.

%package     -n python-%{name}
Summary:        Python libraries and modules for use with gpsd
Provides:       python3-%{name}
%python_provide python3-%{name}

%description -n python-%{name}
Python modules for gpsd.

%package        clients
Summary:        Clients for gpsd
Requires:       python3-%{name} = %{version}-%{release}

%description    clients
Various clients using gpsd.

%package        xclients
Summary:        Graphical clients for gpsd
Requires:       python3-%{name} = %{version}-%{release}
Requires:       python3dist(cairo)
Requires:       python3dist(PyGObject)
Requires:       gtk3

%description    xclients
X clients using gpsd.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
export CCFLAGS="%{optflags}"
export LINKFLAGS="%{__global_ldflags}"

scons %{?_smp_mflags} \
    dbus_export=yes \
    systemd=yes \
    libQgpsmm=yes \
    qt=yes \
    qt_versioned=6 \
    debug=yes \
    leapfetch=no \
    manbuild=no \
    prefix="" \
    sysconfdif=%{_sysconfdir} \
    bindir=%{_bindir} \
    includedir=%{_includedir} \
    libdir=%{_libdir} \
    sbindir=%{_sbindir} \
    mandir=%{_mandir} \
    mibdir=%{_docdir}/gpsd \
    docdir=%{_docdir}/gpsd \
    pkgconfigdir=%{_libdir}/pkgconfig \
    icondir=%{_datadir}/gpsd \
    udevdir=$(pkg-config --variable=udevdir udev) \
    unitdir=%{_unitdir} \
    target_python=python3 \
    python_shebang=%{__python3} \
    python_libdir=%{python3_sitearch} \
    build

%install
export CCFLAGS="%{optflags}"
export LINKFLAGS="%{__global_ldflags}"

DESTDIR=%{buildroot} scons install systemd_install udev-install

install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/sysconfig/gpsd

desktop-file-install --dir %{buildroot}%{_datadir}/applications packaging/X11/xgps.desktop
desktop-file-install --dir %{buildroot}%{_datadir}/applications packaging/X11/xgpsspeed.desktop

install -p -m 0755 gpsinit %{buildroot}%{_sbindir}

%post
%systemd_post gpsd.service gpsd.socket

%preun
%systemd_preun gpsd.service gpsd.socket

%postun
%systemd_postun gpsd.service gpsd.socket

%files
%license COPYING
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_docdir}/gpsd
%{_sbindir}/gpsd
%{_sbindir}/gpsdctl
%{_sbindir}/gpsinit
%{_bindir}/gpsmon
%{_bindir}/gpsctl
%{_bindir}/ntpshmmon
%{_bindir}/ppscheck
%{_unitdir}/gpsd.service
%{_unitdir}/gpsd.socket
%{_unitdir}/gpsdctl@.service
%{_prefix}/lib/udev/rules.d/*.rules
%{_mandir}/man8/gpsd.8*
%{_mandir}/man8/gpsdctl.8*
%{_mandir}/man8/gpsinit.8*
%{_mandir}/man8/ppscheck.8*
%{_mandir}/man1/gpsmon.1*
%{_mandir}/man1/gpsctl.1*
%{_mandir}/man1/ntpshmmon.1*
%{_libdir}/libgps.so.*
%{_libdir}/libQgpsmm.so.*
%{_libdir}/libgpsdpacket.so*

%files devel
%doc TODO HACKING
%{_libdir}/libgps.so
%{_libdir}/libgpsdpacket.so
%{_libdir}/pkgconfig/libgps.pc
%{_includedir}/gps.h
%{_includedir}/libgpsmm.h
%{_mandir}/man3/libgps.3*
%{_mandir}/man3/libgpsmm.3*
%{_mandir}/man5/gpsd_json.5*

%files qt6-devel
%{_libdir}/libQgpsmm.so
%{_libdir}/libQgpsmm.prl
%{_libdir}/pkgconfig/Qgpsmm.pc
%{_mandir}/man3/libQgpsmm.3*

%files -n python-gpsd
%{python3_sitearch}/gps*

%files clients
%{_bindir}/cgps
%{_bindir}/gegps
%{_bindir}/gps2udp
%{_bindir}/gpscat
%{_bindir}/gpscsv
%{_bindir}/gpsdebuginfo
%{_bindir}/gpsdecode
%{_bindir}/gpslogntp
%{_bindir}/gpspipe
%{_bindir}/gpsplot
%{_bindir}/gpsprof
%{_bindir}/gpsrinex
%{_bindir}/gpssnmp
%{_bindir}/gpssubframe
%{_bindir}/gpxlogger
%{_bindir}/lcdgps
%{_bindir}/gpsfake
%{_bindir}/ubxtool
%{_bindir}/zerk
%{_mandir}/man1/gegps.1*
%{_mandir}/man1/gps.1*
%{_mandir}/man1/gps2udp.1*
%{_mandir}/man1/gpscsv.1*
%{_mandir}/man1/gpsdebuginfo.1*
%{_mandir}/man1/gpsdecode.1*
%{_mandir}/man1/gpslogntp.1*
%{_mandir}/man1/gpspipe.1*
%{_mandir}/man1/gpsplot.1*
%{_mandir}/man1/gpsprof.1*
%{_mandir}/man1/gpsrinex.1*
%{_mandir}/man1/gpssnmp.1*
%{_mandir}/man1/gpssubframe.1*
%{_mandir}/man1/gpxlogger.1*
%{_mandir}/man1/lcdgps.1*
%{_mandir}/man1/cgps.1*
%{_mandir}/man1/gpscat.1*
%{_mandir}/man1/gpsfake.1*
%{_mandir}/man1/ubxtool.1*
%{_mandir}/man1/zerk.1*

%files xclients
%{_bindir}/xgps
%{_bindir}/xgpsspeed
%{_datadir}/applications/*.desktop
%dir %{_datadir}/gpsd
%{_datadir}/gpsd/gpsd-logo.png
%{_mandir}/man1/xgps.1*
%{_mandir}/man1/xgpsspeed.1*

%changelog
%autochangelog
