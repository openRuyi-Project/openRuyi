# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           system-config-printer
Version:        1.5.18
Release:        %autorelease
Summary:        A printer administration tool
License:        GPL-2.0-or-later
URL:            https://github.com/OpenPrinting/system-config-printer
#!RemoteAsset:  sha256:811ad6ac010e5c0b938d38b499e7f6e9e95941716b072335a5c99b2a962e9578
Source0:        https://github.com/OpenPrinting/system-config-printer/releases/download/v%{version}/system-config-printer-%{version}.tar.gz
BuildSystem:    autotools

# fix need antomake-1.6 and downlaod xtd file from net.
Patch0:         2000-disable-download-from-net.patch

BuildOption(conf):  --with-udev-rules
BuildOption(conf):  --with-systemdsystemunitdir=%{_unitdir}

BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  intltool
BuildRequires:  gettext-devel
BuildRequires:  autoconf-archive
BuildRequires:  pkgconfig(cups)
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  systemd-rpm-macros
BuildRequires:  xmlto
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  docbook-xsl

Requires:       python3dist(cairo)
Requires:       python3dist(dbus)
Requires:       python3dist(firewall)
Requires:       python3dist(gobject)
Requires:       python3dist(cups)
%{?systemd_requires}

%description
system-config-printer is a graphical user interface that allows
the user to configure a CUPS print server.

%package     -n python-cupshelpers
Summary:        High-level Python Bindings for CUPS
Requires:       python3dist(cups)
Requires:       python3dist(pycurl)
Requires:       python3dist(requests)
BuildArch:      noarch
Provides:       python3-cupshelpers
%python_provide python3-cupshelpers

%description -n python-cupshelpers
This package provides high-level python bindings for CUPS, and can be
used on top of python3-cups.

%install -a
mkdir -p %{buildroot}%{_localstatedir}/run/udev-configure-printer
touch %{buildroot}%{_localstatedir}/run/udev-configure-printer/usb-uris

%py_byte_compile %{__python3} %{buildroot}%{_datadir}/%{name}

%find_lang %{name} --generate-subpackages

%files -f %{name}.lang
%doc ChangeLog NEWS ABOUT-NLS AUTHORS ChangeLog-OLD
%license COPYING
%{_bindir}/system-config-printer
%{_bindir}/install-printerdriver
%{_datadir}/system-config-printer/__pycache__/*
%{_datadir}/system-config-printer/*.py*
%{_datadir}/system-config-printer/troubleshoot
%{_datadir}/system-config-printer/icons
%dir %{_datadir}/system-config-printer/xml/__pycache__
%{_datadir}/system-config-printer/xml/__pycache__/*
%{_datadir}/system-config-printer/xml/validate.py*
%dir %{_datadir}/system-config-printer/ui
%{_datadir}/system-config-printer/ui/*.ui
%{_datadir}/applications/system-config-printer.desktop
%{_datadir}/metainfo/system-config-printer.appdata.xml
%{_mandir}/man1/system-config-printer.1*
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/com.redhat.NewPrinterNotification.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/com.redhat.PrinterDriversInstaller.conf
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/dbus-1/services/*.service
%{_bindir}/scp-dbus-service
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/xml/*.rng
%{_bindir}/system-config-printer-applet
%{_sysconfdir}/xdg/autostart/print-applet.desktop
%{_mandir}/man1/system-config-printer-applet.1*
%{_prefix}/lib/udev/rules.d/*.rules
%{_prefix}/lib/udev/udev-*-printer
%ghost %dir %{_localstatedir}/run/udev-configure-printer
%ghost %verify(not md5 size mtime) %config(noreplace,missingok) %attr(0644,root,root) %{_localstatedir}/run/udev-configure-printer/usb-uris
%{_unitdir}/configure-printer@.service

%files -n python-cupshelpers
%dir %{_sysconfdir}/cupshelpers
%config(noreplace) %{_sysconfdir}/cupshelpers/preferreddrivers.xml
%{python3_sitelib}/*.egg-info/
%exclude %{python3_sitelib}/cupshelpers/__pycache__/*.pyc
%{python3_sitelib}/cupshelpers

%changelog
%autochangelog
