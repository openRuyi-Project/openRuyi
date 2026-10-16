# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xiang W <wangxiang@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           fwupd
Version:        2.1.8
Release:        %autorelease
Summary:        Firmware update daemon
License:        LGPL-2.1-or-later
URL:            https://github.com/fwupd/fwupd
VCS:            git@github.com:fwupd/fwupd.git
#!RemoteAsset:  sha256:29ce4c6d7c5211f487474219474b422132b58f03adedf826816b9c8cce129274
Source0:        https://github.com/fwupd/fwupd/archive/refs/tags/%{version}.tar.gz
BuildSystem:    meson

%ifnarch x86_64
BuildOption(conf):  -Dhsi=disabled
%endif
BuildOption(conf):  -Dpassim=disabled
# missing pkgconfig(umockdev-1.0)
BuildOption(conf):  -Dumockdev_tests=disabled
# missing python3-cairo
BuildOption(conf):  -Dplugin_uefi_capsule_splash=false
BuildOption(conf):  -Defi_os_dir=%{_vendor}

BuildRequires:  cmake
BuildRequires:  meson
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libmnl)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(mm-glib)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(qmi-glib)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(valgrind)
BuildRequires:  pkgconfig(xmlb)
BuildRequires:  python3-jinja2
BuildRequires:  vala

Requires: fwupd-efi
Requires: udisks2
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
A system daemon to allow session software to update firmware

%package devel
Summary: Development package for %{name}
Requires: %{name}

%description devel
Files for development with %{name}.

%package tests
Summary: Data files for installed tests
Requires: %{name}

%description tests
Data files for installed tests.

%install -a
%find_lang %{name} --generate-subpackages

%post
%systemd_post fwupd.service fwupd-refresh.timer

%preun
%systemd_preun fwupd.service fwupd-refresh.timer

%postun
%systemd_postun_with_restart fwupd.service fwupd-refresh.timer

%files -f %{name}.lang
%doc README.md
%license COPYING
%config(noreplace) %{_sysconfdir}/fwupd/fwupd.conf
%config(noreplace) %{_sysconfdir}/fwupd/remotes.d/lvfs.conf
%config(noreplace) %{_sysconfdir}/fwupd/remotes.d/lvfs-embargo.conf
%config(noreplace) %{_sysconfdir}/fwupd/remotes.d/lvfs-testing.conf
%config(noreplace) %{_sysconfdir}/fwupd/remotes.d/vendor-directory.conf
%{_bindir}/dbxtool
%{_bindir}/fwupdmgr
%{_bindir}/fwupdtool
%{_datadir}/dbus-1/interfaces/org.freedesktop.fwupd.xml
%{_datadir}/dbus-1/system.d/org.freedesktop.fwupd.conf
%{_datadir}/dbus-1/system-services/org.freedesktop.fwupd.service
%{_datadir}/fish/vendor_completions.d/fwupdmgr.fish
%{_datadir}/fwupd/add_capsule_header.py
%{_datadir}/fwupd/firmware_packager.py
%{_datadir}/fwupd/install_dell_bios_exe.py
%{_datadir}/fwupd/metainfo/
%{_datadir}/fwupd/quirks.d/builtin.quirk.gz
%{_datadir}/fwupd/remotes.d/vendor/firmware/README.md
%{_datadir}/fwupd/simple_client.py
%{_datadir}/icons/hicolor/128x128/apps/org.freedesktop.fwupd.png
%{_datadir}/icons/hicolor/64x64/apps/org.freedesktop.fwupd.png
%{_datadir}/icons/hicolor/scalable/apps/org.freedesktop.fwupd.svg
%{_datadir}/metainfo/org.freedesktop.fwupd.metainfo.xml
%{_datadir}/polkit-1/actions/org.freedesktop.fwupd.policy
%{_datadir}/polkit-1/rules.d/org.freedesktop.fwupd.rules
%{_libdir}/fwupd-%{version}/*.so
%{_libdir}/girepository-1.0/Fwupd-2.0.typelib
%{_libdir}/libfwupd.so*
%{_libexecdir}/fwupd/fwupd
%{_mandir}/man1/dbxtool.1.gz
%{_mandir}/man1/fwupdmgr.1.gz
%{_mandir}/man1/fwupdtool.1.gz
%{_mandir}/man5/fwupd.conf.5.gz
%{_mandir}/man5/fwupd-remotes.d.5.gz
%{_mandir}/man8/fwupd-refresh.service.8.gz
%{_prefix}/lib/modules-load.d/*.conf
%{_prefix}/lib/systemd/system-shutdown/fwupd.shutdown
%{_prefix}/lib/sysusers.d/fwupd.conf
%{_sysconfdir}/fwupd/bios-settings.d/README.md
%{_sysconfdir}/grub.d/35_fwupd
%{_sysconfdir}/pki/fwupd/LVFS-CA-2025PQ.pem
%{_sysconfdir}/pki/fwupd/LVFS-CA.pem
%{_sysconfdir}/pki/fwupd-metadata/LVFS-CA-2025PQ.pem
%{_sysconfdir}/pki/fwupd-metadata/LVFS-CA.pem
%{_unitdir}/fwupd-refresh.service
%{_unitdir}/fwupd-refresh.timer
%{_unitdir}/fwupd.service

%files devel
%{_datadir}/doc/fwupd/
%{_datadir}/doc/libfwupdplugin/
%{_datadir}/doc/libfwupd/
%{_datadir}/gir-1.0/Fwupd-2.0.gir
%{_datadir}/vala/vapi
%{_libdir}/libfwupd.so
%{_includedir}/fwupd-3
%{_libdir}/pkgconfig/fwupd.pc

%files tests
%{_datadir}/fwupd/host-emulate.d/thinkpad-p1-iommu.json.gz
%{_datadir}/fwupd/remotes.d/fwupd-tests.conf
%{_datadir}/installed-tests/fwupd
%{_libexecdir}/installed-tests/fwupd

%changelog
%autochangelog
