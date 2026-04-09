# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global apiversion   0.3
%global spaversion   0.2

Name:           pipewire
Version:        1.5.84
Release:        %autorelease
Summary:        Media Sharing Server
License:        MIT
URL:            https://gitlab.freedesktop.org/pipewire/pipewire
#!RemoteAsset
Source0:        https://gitlab.freedesktop.org/pipewire/pipewire/-/archive/%{version}/pipewire-%{version}.tar.gz
Source1:        pipewire.sysusers
BuildSystem:    meson

BuildOption(conf):  -Ddocs=enabled
BuildOption(conf):  -Dman=enabled
BuildOption(conf):  -Dgstreamer=enabled
BuildOption(conf):  -Dsystemd-user-service=enabled
BuildOption(conf):  -Dsdl2=enabled
BuildOption(conf):  -Daudiotestsrc=enabled
BuildOption(conf):  -Dvideotestsrc=enabled
BuildOption(conf):  -Dvolume=enabled
BuildOption(conf):  -Dbluez5-codec-aptx=disabled
BuildOption(conf):  -Dbluez5-codec-lc3plus=disabled
BuildOption(conf):  -Dbluez5-codec-lc3=enabled
BuildOption(conf):  -Dsession-managers=[]
BuildOption(conf):  -Davahi=enabled
BuildOption(conf):  -Dx11=enabled
BuildOption(conf):  -Dx11-xfixes=disabled
BuildOption(conf):  -Dlibcanberra=enabled
BuildOption(conf):  -Dgstreamer-device-provider=enabled
BuildOption(conf):  -Decho-cancel-webrtc=disabled
BuildOption(conf):  -Dbluez5=disabled
BuildOption(conf):  -Dsnap=disabled
BuildOption(conf):  -Decho-cancel-webrtc=disabled
BuildOption(conf):  -Debur128=disabled
BuildOption(conf):  -Donnxruntime=disabled
BuildOption(conf):  -Dpipewire-jack=enabled
BuildOption(conf):  -Djack-devel=false
BuildOption(conf):  -Djack=enabled
BuildOption(conf):  -Dlibcamera=disabled
BuildOption(conf):  -Dpipewire-alsa=enabled
BuildOption(conf):  -Dvulkan=enabled
BuildOption(conf):  -Dlibmysofa=disabled
BuildOption(conf):  -Dlv2=disabled
BuildOption(conf):  -Droc=disabled
BuildOption(conf):  -Dlibffado=disabled

BuildRequires:  meson >= 0.59.0
BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  gettext
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.32
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.10.0
BuildRequires:  pkgconfig(gstreamer-base-1.0) >= 1.10.0
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0) >= 1.10.0
BuildRequires:  pkgconfig(gstreamer-net-1.0) >= 1.10.0
BuildRequires:  pkgconfig(gstreamer-allocators-1.0) >= 1.10.0
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(bluez)
BuildRequires:  pkgconfig(fdk-aac)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(speexdsp)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  doxygen
BuildRequires:  python3-docutils
BuildRequires:  graphviz
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(avahi-core)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(libcanberra)

Requires:       systemd
Requires:       rtkit

%description
PipeWire is a multimedia server for Linux.

%package        devel
Summary:        Headers and libraries for PipeWire client development
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development headers for PipeWire.

%install -a
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/pipewire.conf

install -d -m 0755 %{buildroot}%{_datadir}/pipewire/pipewire.conf.d/
install -d -m 0755 %{buildroot}%{_datadir}/pipewire/client.conf.d/

mkdir -p %{buildroot}%{_sysconfdir}/alsa/conf.d/
cp %{buildroot}%{_datadir}/alsa/alsa.conf.d/50-pipewire.conf \
        %{buildroot}%{_sysconfdir}/alsa/conf.d/50-pipewire.conf
cp %{buildroot}%{_datadir}/alsa/alsa.conf.d/99-pipewire-default.conf \
        %{buildroot}%{_sysconfdir}/alsa/conf.d/99-pipewire-default.conf

install -d -m 0755 %{buildroot}%{_datadir}/pipewire/pipewire-pulse.conf.d/
ln -s ../pipewire-pulse.conf.avail/20-upmix.conf \
        %{buildroot}%{_datadir}/pipewire/pipewire-pulse.conf.d/20-upmix.conf
# rates config
ln -s ../pipewire.conf.avail/10-rates.conf \
        %{buildroot}%{_datadir}/pipewire/pipewire.conf.d/10-rates.conf
# upmix config
ln -s ../pipewire.conf.avail/20-upmix.conf \
        %{buildroot}%{_datadir}/pipewire/pipewire.conf.d/20-upmix.conf
ln -s ../client.conf.avail/20-upmix.conf \
        %{buildroot}%{_datadir}/pipewire/client.conf.d/20-upmix.conf
# raop config
ln -s ../pipewire.conf.avail/50-raop.conf \
        %{buildroot}%{_datadir}/pipewire/pipewire.conf.d/50-raop.conf
# todo: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*

%find_lang %{name} --generate-subpackages

%post
%systemd_user_post pipewire.service pipewire.socket
%systemd_user_post pipewire-pulse.service pipewire-pulse.socket

%files -f %{name}.lang
%license LICENSE COPYING
%doc README.md NEWS
%{_userunitdir}/pipewire.*
%{_userunitdir}/filter-chain.*
%{_bindir}/pipewire
%{_bindir}/pipewire-avb
%{_bindir}/pipewire-aes67
%{_bindir}/pipewire-vulkan
%{_mandir}/man1/*
%dir %{_datadir}/pipewire/
%dir %{_datadir}/pipewire/pipewire.conf.d/
%{_datadir}/pipewire/pipewire.conf
%{_datadir}/pipewire/pipewire.conf.avail/10-rates.conf
%{_datadir}/pipewire/pipewire.conf.avail/20-upmix.conf
%{_datadir}/pipewire/pipewire.conf.avail/50-raop.conf
%{_datadir}/pipewire/minimal.conf
%{_datadir}/pipewire/filter-chain.conf
%{_datadir}/pipewire/filter-chain/*.conf
%{_datadir}/pipewire/pipewire-avb.conf
%{_datadir}/pipewire/pipewire-aes67.conf
%{_datadir}/pipewire/pipewire-vulkan.conf
%config(noreplace) %{_sysconfdir}/security/limits.d/*.conf
%{_sysusersdir}/pipewire.conf
# libs
%{_libdir}/libpipewire-%{apiversion}.so.*
%{_libdir}/pipewire-%{apiversion}/jack/libjack*.so.*
%{_libdir}/pipewire-%{apiversion}/libpipewire-module-access.so
%{_libdir}/pipewire-%{apiversion}/libpipewire-module-adapter.so
%{_libdir}/pipewire-%{apiversion}/libpipewire-module-avb.so
%{_libdir}/pipewire-%{apiversion}/libpipewire-module-client-device.so
%{_libdir}/pipewire-%{apiversion}/libpipewire-module-client-node.so
%{_libdir}/pipewire-%{apiversion}/libpipewire-module-combine-stream.so
%{_libdir}/pipewire-%{apiversion}/libpipewire-module-echo-cancel.so
%{_libdir}/pipewire-%{apiversion}/libpipewire-module-fallback-sink.so
%{_libdir}/pipewire-%{apiversion}/libpipewire-module-filter-chain.so
%{_libdir}/pipewire-%{apiversion}/libpipewire-module-link-factory.so
%{_libdir}/pipewire-%{apiversion}/libpipewire-module-loopback.so
%{_libdir}/pipewire-%{apiversion}/libpipewire-module-metadata.so
%{_libdir}/pipewire-%{apiversion}/libpipewire-module-netjack2-driver.so
%{_libdir}/pipewire-%{apiversion}/libpipewire-module-netjack2-manager.so
%{_libdir}/pipewire-%{apiversion}/libpipewire-module-parametric-equalizer.so
%{_libdir}/pipewire-%{apiversion}/libpipewire-module-pipe-tunnel.so
%{_libdir}/pipewire-%{apiversion}/libpipewire-module-portal.so
%{_libdir}/pipewire-%{apiversion}/libpipewire-module-profiler.so
%{_libdir}/pipewire-%{apiversion}/libpipewire-module-protocol-native.so
%{_libdir}/pipewire-%{apiversion}/libpipewire-module-protocol-simple.so
%{_libdir}/pipewire-%{apiversion}/libpipewire-module-pulse-tunnel.so
%{_libdir}/pipewire-%{apiversion}/libpipewire-module-raop-sink.so
%{_libdir}/pipewire-%{apiversion}/libpipewire-module-rtkit.so
%{_libdir}/pipewire-%{apiversion}/libpipewire-module-rtp-sap.so
%{_libdir}/pipewire-%{apiversion}/libpipewire-module-rtp-sink.so
%{_libdir}/pipewire-%{apiversion}/libpipewire-module-rtp-source.so
%{_libdir}/pipewire-%{apiversion}/libpipewire-module-rt.so
%{_libdir}/pipewire-%{apiversion}/libpipewire-module-session-manager.so
%{_libdir}/pipewire-%{apiversion}/libpipewire-module-spa-device-factory.so
%{_libdir}/pipewire-%{apiversion}/libpipewire-module-spa-device.so
%{_libdir}/pipewire-%{apiversion}/libpipewire-module-spa-node-factory.so
%{_libdir}/pipewire-%{apiversion}/libpipewire-module-spa-node.so
%{_libdir}/pipewire-%{apiversion}/libpipewire-module-vban-send.so
%{_libdir}/pipewire-%{apiversion}/libpipewire-module-vban-recv.so
%{_libdir}/pipewire-%{apiversion}/libpipewire-module-jack-tunnel.so
%{_libdir}/pipewire-%{apiversion}/libpipewire-module-jackdbus-detect.so
%{_libdir}/pipewire-%{apiversion}/libpipewire-module-raop-discover.so
%{_libdir}/pipewire-%{apiversion}/libpipewire-module-rtp-session.so
%{_libdir}/pipewire-%{apiversion}/libpipewire-module-snapcast-discover.so
%{_libdir}/pipewire-%{apiversion}/libpipewire-module-x11-bell.so
%{_libdir}/pipewire-%{apiversion}/libpipewire-module-zeroconf-discover.so
%dir %{_datadir}/alsa-card-profile/
%dir %{_datadir}/alsa-card-profile/mixer/
%{_datadir}/alsa-card-profile/mixer/paths/
%{_datadir}/alsa-card-profile/mixer/profile-sets/
%{_prefix}/lib/udev/rules.d/90-pipewire-alsa.rules
%dir %{_libdir}/spa-%{spaversion}
%{_libdir}/spa-%{spaversion}/aec/
%{_libdir}/spa-%{spaversion}/alsa/
%{_libdir}/spa-%{spaversion}/audioconvert/
%{_libdir}/spa-%{spaversion}/audiomixer/
%{_libdir}/spa-%{spaversion}/avb/
%{_libdir}/spa-%{spaversion}/control/
%{_libdir}/spa-%{spaversion}/audiotestsrc/
%{_libdir}/spa-%{spaversion}/videotestsrc/
%{_libdir}/spa-%{spaversion}/volume/
%{_libdir}/spa-%{spaversion}/filter-graph/libspa-filter-graph.so
%{_libdir}/spa-%{spaversion}/filter-graph/libspa-filter-graph-plugin-builtin.so
%{_libdir}/spa-%{spaversion}/filter-graph/libspa-filter-graph-plugin-ladspa.so
%{_libdir}/spa-%{spaversion}/jack/libspa-jack.so
%{_libdir}/spa-%{spaversion}/support/
%{_libdir}/spa-%{spaversion}/v4l2/
%{_libdir}/spa-%{spaversion}/videoconvert/
%{_libdir}/spa-%{spaversion}/libspa.so
%{_datadir}/pipewire/client.conf
%dir %{_datadir}/pipewire/client.conf.d/
%{_datadir}/pipewire/client.conf.avail/20-upmix.conf
# gstreamer
%{_libdir}/gstreamer-1.0/libgstpipewire.*
# doc
%{_datadir}/doc/pipewire/html
# utils
%{_bindir}/pw-cat
%{_bindir}/pw-jack
%{_bindir}/pw-cli
%{_bindir}/pw-config
%{_bindir}/pw-container
%{_bindir}/pw-dot
%{_bindir}/pw-dsdplay
%{_bindir}/pw-dump
%{_bindir}/pw-encplay
%{_bindir}/pw-link
%{_bindir}/pw-loopback
%{_bindir}/pw-metadata
%{_bindir}/pw-mididump
%{_bindir}/pw-midiplay
%{_bindir}/pw-midirecord
%{_bindir}/pw-midi2play
%{_bindir}/pw-midi2record
%{_bindir}/pw-mon
%{_bindir}/pw-play
%{_bindir}/pw-profiler
%{_bindir}/pw-record
%{_bindir}/pw-reserve
%{_bindir}/pw-sysex
%{_bindir}/pw-top
%{_bindir}/spa*
# alsa
%{_libdir}/alsa-lib/libasound_module_pcm_pipewire.so
%{_libdir}/alsa-lib/libasound_module_ctl_pipewire.so
%{_datadir}/alsa/alsa.conf.d/50-pipewire.conf
%{_datadir}/alsa/alsa.conf.d/99-pipewire-default.conf
%config(noreplace) %{_sysconfdir}/alsa/conf.d/50-pipewire.conf
%config(noreplace) %{_sysconfdir}/alsa/conf.d/99-pipewire-default.conf
# vulkan
%{_libdir}/spa-%{spaversion}/vulkan/
# pulseaudio
%{_bindir}/pipewire-pulse
%{_userunitdir}/pipewire-pulse.*
%{_datadir}/pipewire/pipewire-pulse.conf
%dir %{_datadir}/pipewire/pipewire-pulse.conf.d/
%{_datadir}/pipewire/pipewire-pulse.conf.avail/20-upmix.conf
%{_datadir}/glib-2.0/schemas/org.freedesktop.pulseaudio.gschema.xml
%{_libdir}/pipewire-%{apiversion}/libpipewire-module-protocol-pulse.so
%{_mandir}/man5/*
%{_mandir}/man7/*
# v412
%{_bindir}/pw-v4l2
%{_libdir}/pipewire-%{apiversion}/v4l2/libpw-v4l2.so
# other
%{_datadir}/pipewire/pipewire.conf.d/50-raop.conf
%{_datadir}/pipewire/pipewire.conf.d/10-rates.conf
%{_datadir}/pipewire/pipewire.conf.d/20-upmix.conf
%{_datadir}/pipewire/client.conf.d/20-upmix.conf
%{_datadir}/pipewire/pipewire-pulse.conf.d/20-upmix.conf
%{_datadir}/pipewire/jack.conf

%files devel
%{_libdir}/libpipewire-%{apiversion}.so
%{_includedir}/pipewire-%{apiversion}/
%{_includedir}/spa-%{spaversion}/
%{_libdir}/pipewire-%{apiversion}/jack/libjack.so
%{_libdir}/pipewire-%{apiversion}/jack/libjacknet.so
%{_libdir}/pipewire-%{apiversion}/jack/libjackserver.so
%{_libdir}/pkgconfig/libpipewire-%{apiversion}.pc
%{_libdir}/pkgconfig/libspa-%{spaversion}.pc

%changelog
%autochangelog
