# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Yifan Xu <xuyifan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           remmina
Version:        1.4.43
Release:        %autorelease
Summary:        Remote desktop client written in GTK with RDP and VNC support
License:        GPL-2.0-or-later
URL:            https://www.remmina.org
VCS:            git:https://gitlab.com/Remmina/Remmina.git
#!RemoteAsset:  sha256:16533f8a806daff524649bb45ae51e51f61685da94846006018b3c279ebe7035
Source0:        https://gitlab.com/Remmina/Remmina/-/archive/v%{version}/Remmina-v%{version}.tar.gz#/remmina-%{version}.tar.gz
# Port the KWallet credential plugin from KF5 to KF6.
# https://gitweb.gentoo.org/repo/gentoo.git/tree/net-misc/remmina/files/remmina-1.4.40-kf6wallet.patch
Patch:          2001-switch-kf5wallet-to-kf6wallet.patch
BuildSystem:    cmake

# The upstream GitLab source archive extracts into a directory named after the
# repository and tag rather than the default Name-Version layout expected by
# the automatic unpack stage.
BuildOption(prep):  -n Remmina-v%{version}

BuildOption(conf):  -DWITH_FREERDP3=ON
# browser plugin need gtk2webkit
BuildOption(conf):  -DWITH_WWW=OFF
BuildOption(conf):  -DWITH_NEWS=OFF
BuildOption(conf):  -DWITH_KF6WALLET=ON
# we have no x2go and gvnc
BuildOption(conf):  -DWITH_X2GO=OFF
BuildOption(conf):  -DWITH_GVNC=OFF

# The Python wrapper plugin is not needed for the core remote desktop feature
# set and would drag the Python interpreter into the package.
BuildOption(conf):  -DWITH_PYTHONLIBS=OFF

# Upstream links appindicator unconditionally for the tray status icon when
# this option is on, but neither appindicator nor ayatana-appindicator is
# packaged in openRuyi yet. Turning it off only drops the tray icon feature.
BuildOption(conf):  -DHAVE_LIBAPPINDICATOR=OFF

BuildRequires:      cmake
BuildRequires:      gettext
BuildRequires:      pkgconfig(cups)
BuildRequires:      pkgconfig(openssl)
BuildRequires:      kf6-kwallet-devel
BuildRequires:      pkgconfig(avahi-ui-gtk3)
BuildRequires:      pkgconfig(freerdp3)
BuildRequires:      pkgconfig(gio-unix-2.0)
BuildRequires:      pkgconfig(glib-2.0)
BuildRequires:      pkgconfig(gtk+-3.0)
BuildRequires:      pkgconfig(harfbuzz)
BuildRequires:      pkgconfig(json-glib-1.0)
BuildRequires:      pkgconfig(libcurl)
BuildRequires:      pkgconfig(libgcrypt)
BuildRequires:      pkgconfig(libpcre2-8)
BuildRequires:      pkgconfig(libsecret-1)
BuildRequires:      pkgconfig(libsodium)
BuildRequires:      pkgconfig(libssh)
BuildRequires:      pkgconfig(libvncclient)
BuildRequires:      pkgconfig(libvncserver)
BuildRequires:      pkgconfig(vte-2.91)
BuildRequires:      pkgconfig(wayland-client)
BuildRequires:      pkgconfig(xkbcommon)
BuildRequires:      pkgconfig(gdk-pixbuf-2.0)
Requires:           gdk-pixbuf

%description
Remmina is a modern remote desktop client written in GTK. It supports multiple
network protocols in a unified, modular user interface, including:

* RDP (Remote Desktop Protocol) through FreeRDP 3
* VNC through LibVNCClient, with SSH tunneling
* SSH and SFTP terminal sessions through libssh and VTE
* External tool execution (EXEC plugins)

Connections can be organized in profiles, grouped, and quick-launched from the
system menu. Credentials are securely stored through the secret service, with
optional password obfuscation via libgcrypt and libsodium.

%package plugin-kwallet
Summary:            KDE Wallet credential plugin for remmina
Requires:           %{name}%{?_isa} = %{version}-%{release}

%description plugin-kwallet
This package provides the Remmina plugin that stores connection credentials in
the KDE Wallet, the credential store of the KDE Plasma desktop, using KDE
Frameworks 6.

%package devel
Summary:            Development files for remmina
Requires:           %{name}%{?_isa} = %{version}-%{release}
Requires:           pkgconfig(gtk+-3.0)

%description devel
This package provides the header files and pkg-config metadata needed to
develop third-party protocol plugins for Remmina.

%install -a
# Collect translated .mo files instead of brute-force globbing the locale tree.
%find_lang %{name}

%files -f %{name}.lang
%license LICENSE LICENSE.OpenSSL
%doc README.md CHANGELOG.md AUTHORS
%{_bindir}/remmina
%{_bindir}/remmina-file-wrapper
%dir %{_libdir}/remmina
%dir %{_libdir}/remmina/plugins
%{_libdir}/remmina/plugins/remmina-plugin-exec.so
%{_libdir}/remmina/plugins/remmina-plugin-rdp.so
%{_libdir}/remmina/plugins/remmina-plugin-secret.so
%{_libdir}/remmina/plugins/remmina-plugin-vnc.so
%{_datadir}/applications/org.remmina.Remmina.desktop
%{_datadir}/applications/org.remmina.Remmina-file.desktop
%{_datadir}/icons/hicolor/
%{_datadir}/metainfo/org.remmina.Remmina.appdata.xml
%{_datadir}/mime/packages/org.remmina.Remmina-mime.xml
%{_datadir}/remmina/
%{_mandir}/man1/remmina.1%{?ext_man}
%{_mandir}/man1/remmina-file-wrapper.1%{?ext_man}

%files plugin-kwallet
%{_libdir}/remmina/plugins/remmina-plugin-kwallet.so

%files devel
%{_includedir}/remmina/
%{_libdir}/pkgconfig/remmina.pc

%changelog
%autochangelog
