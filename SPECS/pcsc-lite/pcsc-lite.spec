# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           pcsc-lite
Version:        2.3.3
Release:        %autorelease
Summary:        Middleware to access a smart card using SCard API (PC/SC)
License:        BSD-3-Clause
URL:            https://pcsclite.apdu.fr/
VCS:            git:https://github.com/LudovicRousseau/PCSC.git
#!RemoteAsset:  sha256:cdff7d7153a0b37aa74e26dfec89ec7dc5c5286aa21b91b903e38739d227e8e7
Source:         https://pcsclite.apdu.fr/files/pcsc-lite-%{version}.tar.xz
BuildSystem:    meson

BuildOption(conf):  -Dpolkit=true
BuildOption(conf):  -Dusbdropdir=%{_libdir}/pcsc/drivers
BuildOption(conf):  -Dlibsystemd=true

BuildRequires:  doxygen
BuildRequires:  meson
BuildRequires:  python3
BuildRequires:  flex
BuildRequires:  duktape
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(mount)

Requires:       polkit
Requires(post):  systemd
Requires(preun):  systemd
Requires(postun):  systemd

Recommends:     ccid

%description
PC/SC Lite is a middleware to access a smart card using SCard API (PC/SC).
This package contains the PC/SC Lite server, runtime library, and utilities.

%package        devel
Summary:        PC/SC Lite library and header files for development
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(libudev)

%description    devel
This package includes the PC/SC Lite library, header files, and API
documentation for development.

%prep -a
for file in ChangeLog; do
    iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
    touch -r $file $file.new && \
    mv $file.new $file
done

%install -a
install -d %{buildroot}%{_sysconfdir}/reader.conf.d

%post
%systemd_post pcscd.socket pcscd.service

%preun
%systemd_preun pcscd.socket pcscd.service

%postun
%systemd_postun_with_restart pcscd.socket pcscd.service

%files
%doc AUTHORS ChangeLog HELP README SECURITY
%doc doc/README.polkit
%{_docdir}/pcsc-lite/setup_spy.sh
%license COPYING
%config(noreplace) %{_sysconfdir}/default/pcscd
%dir %{_sysconfdir}/reader.conf.d/
%ghost %dir %{_localstatedir}/run/pcscd/
%{_libdir}/lib*.so.*
%{_sbindir}/pcscd
%{_userunitdir}/pcscd.socket
%{_userunitdir}/pcscd.service
%{_datadir}/metainfo/fr.apdu.pcsclite.metainfo.xml
%{_datadir}/polkit-1/actions/org.debian.pcsc-lite.policy
%{_mandir}/man5/reader.conf.5*
%{_mandir}/man8/pcscd.8*

%files devel
%{_bindir}/pcsc-spy
%{_includedir}/PCSC/
%{_libdir}/lib*.a
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/libpcsclite.pc
%{_mandir}/man1/*

%changelog
%autochangelog
