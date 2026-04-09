# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond webrtc 0

Name:           pulseaudio
Summary:        Improved Linux Sound Server
Version:        17.0
Release:        %autorelease
License:        LGPL-2.1-or-later
URL:            https://gitlab.freedesktop.org/pulseaudio/pulseaudio
#!RemoteAsset
Source0:        http://freedesktop.org/software/pulseaudio/releases/pulseaudio-%{version}.tar.xz
Source1:        pulseaudio.sysusers
BuildSystem:    meson

# ../src/tests/once-test.c:72:F:once:once_test:0:
# Assertion 'pthread_setaffinity_np(pthread_self(), sizeof(mask), &mask) == 0' failed
# fail in qemu-system.
Patch0:         0001-skip-a-fail-test.patch

BuildOption(conf):  -Dclient=true
BuildOption(conf):  -Dvalgrind=disabled
BuildOption(conf):  -Dsystemd=enabled
BuildOption(conf):  -Doss-output=enabled
BuildOption(conf):  -Dgtk=disabled
BuildOption(conf):  -Dtcpwrap=disabled
BuildOption(conf):  -Delogind=disabled
BuildOption(conf):  -Dconsolekit=disabled
BuildOption(conf):  -Dsoxr=disabled
BuildOption(conf):  -Dasyncns=disabled
BuildOption(conf):  -Dtests=true
BuildOption(conf):  -Ddoxygen=true
BuildOption(conf):  -Djack=disabled
BuildOption(conf):  -Dlirc=disabled
BuildOption(conf):  -Ddaemon=true
BuildOption(conf):  -Dsystem_user=pulse
BuildOption(conf):  -Dsystem_group=pulse
BuildOption(conf):  -Daccess_group=pulse-access
BuildOption(conf):  -Dbluez5=disabled
BuildOption(conf):  -Dgstreamer=enabled
BuildOption(conf):  -Dbluez5-gstreamer=disabled
BuildOption(conf):  -Dgsettings=enabled
BuildOption(conf):  -Davahi=disabled
%if %{with webrtc}
BuildOption(conf):  -Dwebrtc-aec=enabled
%else
BuildOption(conf):  -Dwebrtc-aec=disabled
%endif
BuildOption(conf):  -Dorc=disabled

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  m4
BuildRequires:  pkgconfig
BuildRequires:  gettext
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(fftw3f)
BuildRequires:  libtool
BuildRequires:  pkgconfig(libcap)
BuildRequires:  perl-XML-Parser
BuildRequires:  xmltoman
BuildRequires:  pkgconfig(bluez)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(tdb)
BuildRequires:  pkgconfig(speexdsp) >= 1.2
BuildRequires:  pkgconfig(libsystemd) >= 184
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.16.0
BuildRequires:  pkgconfig(gstreamer-app-1.0) >= 1.16.0
BuildRequires:  pkgconfig(gstreamer-rtp-1.0) >= 1.16.0
BuildRequires:  doxygen
BuildRequires:  xmltoman
BuildRequires:  pkgconfig(check)
%if %{with webrtc}
BuildRequires:  pkgconfig(webrtc-audio-processing-1) >= 1.0
%endif

Requires:       rtkit

%description
PulseAudio is a sound server for Linux.

%package        devel
Summary:        Headers and libraries for PulseAudio client development
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers and libraries for developing applications that can communicate with
a PulseAudio sound server.

%install -a
install -m0644 -D %{SOURCE1} %{buildroot}%{_sysusersdir}/pulseaudio.conf

mkdir -p %{buildroot}%{_prefix}/lib/udev/rules.d
mv -fv %{buildroot}/lib/udev/rules.d/90-pulseaudio.rules %{buildroot}%{_prefix}/lib/udev/rules.d

# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
%find_lang %{name} --generate-subpackages

%pre
%sysusers_create_package %{name} %{SOURCE2}

%post
%systemd_user_post pulseaudio.socket pulseaudio.service

%preun
%systemd_user_preun pulseaudio.socket pulseaudio.service

%files
%doc README
%license LICENSE GPL LGPL
%config(noreplace) %{_sysconfdir}/pulse/daemon.conf
%config(noreplace) %{_sysconfdir}/pulse/default.pa
%config(noreplace) %{_sysconfdir}/pulse/system.pa
%config(noreplace) %{_sysconfdir}/pulse/client.conf
%config(noreplace) %{_sysconfdir}/xdg/autostart/pulseaudio.desktop
%config(noreplace) %{_sysconfdir}/xdg/Xwayland-session.d/00-pulseaudio-x11
%{_userunitdir}/pulseaudio.service
%{_userunitdir}/pulseaudio.socket
%{_userunitdir}/pulseaudio-x11.service
%{_libdir}/pulseaudio/libpulsecore-*.so
%dir %{_libdir}/pulseaudio/
%dir %{_libdir}/pulseaudio/modules/
%dir %{_datadir}/pulseaudio/
%dir %{_sysconfdir}/pulse/
%dir %{_libexecdir}/pulse
%dir %{_datadir}/zsh/
%dir %{_datadir}/zsh/site-functions/
%{_datadir}/pulseaudio/alsa-mixer/
%{_datadir}/dbus-1/system.d/pulseaudio-system.conf
%{_datadir}/GConf/gsettings/pulseaudio.convert
%{_datadir}/glib-2.0/schemas/org.freedesktop.pulseaudio.gschema.xml
%{_datadir}/bash-completion/completions/pa*
%{_datadir}/zsh/site-functions/_pulseaudio
%{_datadir}/bash-completion/completions/pulseaudio
%{_udevrulesdir}/90-pulseaudio.rules
%{_sysusersdir}/pulseaudio.conf
%{_libdir}/pulseaudio/modules/lib*.so
%{_libdir}/pulseaudio/modules/module-*.so
%{_libdir}/libpulse.so.*
%{_libdir}/libpulse-simple.so.*
%{_libdir}/pulseaudio/libpulsecommon-*.so
%{_libdir}/pulseaudio/libpulsedsp.so
%{_libdir}/libpulse-mainloop-glib.so.0*
%{_libexecdir}/pulse/gsettings-helper
%{_bindir}/start-pulseaudio-x11
%{_bindir}/pulseaudio
%{_bindir}/pacmd
%{_bindir}/pasuspender
%{_bindir}/qpaeq
%{_bindir}/pa-info
%{_bindir}/pacat
%{_bindir}/pactl
%{_bindir}/paplay
%{_bindir}/parec
%{_bindir}/pamon
%{_bindir}/parecord
%{_bindir}/pax11publish
%{_bindir}/padsp
%{_mandir}/man1/pa*.1*
%{_mandir}/man5/pulse-client.conf.5*
%{_mandir}/man1/pulseaudio.1*
%{_mandir}/man5/default.pa.5*
%{_mandir}/man5/pulse-cli-syntax.5*
%{_mandir}/man5/pulse-daemon.conf.5*
%{_mandir}/man1/start-pulseaudio-x11.1*

%files devel
%{_includedir}/pulse/
%{_libdir}/libpulse.so
%{_libdir}/libpulse-mainloop-glib.so
%{_libdir}/libpulse-simple.so
%{_libdir}/pkgconfig/libpulse*.pc
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libpulse*.vapi
%{_datadir}/vala/vapi/libpulse*.deps
%{_libdir}/cmake/PulseAudio/

%changelog
%autochangelog
