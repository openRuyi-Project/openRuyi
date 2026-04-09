# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond enable_sane 0
%bcond tests 0
%bcond doc 0

Name:           colord
Version:        1.4.8
Release:        %autorelease
Summary:        Color daemon
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://gitlab.freedesktop.org/colord/colord
#!RemoteAsset
Source0:        https://www.freedesktop.org/software/colord/releases/colord-%{version}.tar.xz
Source1:        colord.sysusers
BuildSystem:    meson

BuildOption(conf):  -Ddaemon_user=colord
BuildOption(conf):  -Dlibcolordcompat=false
BuildOption(conf):  -Dargyllcms_sensor=false
BuildOption(conf):  -Dbash_completion=false
BuildOption(conf):  -Dprint_profiles=false
%if %{with enable_sane}
BuildOption(conf):  -Dsane=true
%else
BuildOption(conf):  -Dsane=false
%endif
%if %{with doc}
BuildOption(conf):  -Ddocs=true
BuildOption(conf):  -Dman=true
%else
BuildOption(conf):  -Ddocs=false
BuildOption(conf):  -Dman=false
%endif
%if %{with tests}
BuildOption(conf):  -Dtests=true
BuildOption(conf):  -Dinstalled_tests=true
%else
BuildOption(conf):  -Dtests=false
BuildOption(conf):  -Dinstalled_tests=false
%endif
BuildOption(conf):  -Dvapi=true

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  vala
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(gusb) >= 0.2.7
BuildRequires:  pkgconfig(lcms2) >= 2.6
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(polkit-gobject-1) >= 0.103
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
BuildRequires:  color-rpm-macros
%if %{with doc}
BuildRequires:  gtk-doc
BuildRequires:  docbook-xsl
BuildRequires:  libxslt
%endif
%if %{with enable_sane}
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(sane-backends)
%endif

Requires:       color-rpm-macros

%description
colord is a low level system activated daemon that maps color devices
to color profiles in the system context.

%package        devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Files for development with %{name}.

%if %{with tests}
%package        tests
Summary:        Data files for installed tests

%description    tests
Data files for installed tests.
%endif

%install -a
touch %{buildroot}%{_localstatedir}/lib/colord/mapping.db
touch %{buildroot}%{_localstatedir}/lib/colord/storage.db
install -Dpm0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/colord-sysusers.conf

# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
%find_lang %{name} --generate-subpackages

%pre
%sysusers_create_package %{name} %{SOURCE1}

%post
%systemd_post colord.service

%preun
%systemd_preun colord.service

%postun
%systemd_postun colord.service

%files -f %{name}.lang
%license COPYING
%doc README.md AUTHORS NEWS
%{_libexecdir}/colord
%attr(755,colord,colord) %dir %{_localstatedir}/lib/colord
%attr(755,colord,colord) %dir %{_localstatedir}/lib/colord/icc
%{_bindir}/*
%{_datadir}/glib-2.0/schemas/org.freedesktop.ColorHelper.gschema.xml
%{_datadir}/dbus-1/system.d/org.freedesktop.ColorManager.conf
%{_datadir}/dbus-1/interfaces/org.freedesktop.ColorManager*.xml
%{_datadir}/polkit-1/actions/org.freedesktop.color.policy
%{_datadir}/dbus-1/system-services/org.freedesktop.ColorManager.service
%{_datadir}/metainfo/org.freedesktop.colord.metainfo.xml
%{_datadir}/colord
# udev rules
%{_udevrulesdir}/*.rules
%{_tmpfilesdir}/colord.conf
%{_libdir}/colord-sensors
%{_libdir}/colord-plugins
%ghost %attr(-,colord,colord) %{_localstatedir}/lib/colord/*.db
%{_unitdir}/colord.service
%{_sysusersdir}/colord-sysusers.conf
%{_libexecdir}/colord-session
%{_datadir}/dbus-1/interfaces/org.freedesktop.ColorHelper.xml
%{_datadir}/dbus-1/services/org.freedesktop.ColorHelper.service
%{_userunitdir}/colord-session.service
%if %{with enable_sane}
%{_libexecdir}/colord-sane
%endif
%dir %{_icccolordir}/colord
%{_icccolordir}/colord/AdobeRGB1998.icc
%{_icccolordir}/colord/ProPhotoRGB.icc
%{_icccolordir}/colord/Rec709.icc
%{_icccolordir}/colord/SMPTE-C-RGB.icc
%{_icccolordir}/colord/sRGB.icc
%{_icccolordir}/colord/Bluish.icc
%{_icccolordir}/colord/x11-colors.icc
%{_libdir}/libcolord.so.2*
%{_libdir}/libcolordprivate.so.2*
%{_libdir}/libcolorhug.so.2*
%{_libdir}/girepository-1.0/*.typelib
%if %{with doc}
%{_mandir}/man1/*.1*
%endif
%{_icccolordir}/colord/AppleRGB.icc
%{_icccolordir}/colord/BestRGB.icc
%{_icccolordir}/colord/BetaRGB.icc
%{_icccolordir}/colord/BruceRGB.icc
%{_icccolordir}/colord/CIE-RGB.icc
%{_icccolordir}/colord/ColorMatchRGB.icc
%{_icccolordir}/colord/DonRGB4.icc
%{_icccolordir}/colord/ECI-RGBv1.icc
%{_icccolordir}/colord/ECI-RGBv2.icc
%{_icccolordir}/colord/EktaSpacePS5.icc
%{_icccolordir}/colord/Gamma*.icc
%{_icccolordir}/colord/NTSC-RGB.icc
%{_icccolordir}/colord/PAL-RGB.icc
%{_icccolordir}/colord/SwappedRedAndGreen.icc
%{_icccolordir}/colord/WideGamutRGB.icc
%{_icccolordir}/colord/Crayons.icc

%files devel
%{_includedir}/colord-1
%{_libdir}/libcolord.so
%{_libdir}/libcolordprivate.so
%{_libdir}/libcolorhug.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*.gir
%{_datadir}/vala/vapi/colord.vapi
%{_datadir}/vala/vapi/colord.deps
%if %{with doc}
%doc %{_datadir}/gtk-doc/html/colord
%endif

%if %{with tests}
%files tests
%dir %{_libexecdir}/installed-tests/colord
%{_libexecdir}/installed-tests/colord/*
%dir %{_datadir}/installed-tests/colord
%{_datadir}/installed-tests/colord/*
%endif

%changelog
%autochangelog
