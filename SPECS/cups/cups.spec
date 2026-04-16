# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Dingli Zhang <dingli@iscas.ac.cn>
# SPDX-FileContributor: Jingkun Zheng <zhengjingkun@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global cups_serverbin %{_exec_prefix}/lib/cups

Name:           cups
Version:        2.4.16
Release:        %autorelease
Summary:        Standards-based, open source printing system for Linux
License:        Apache-2.0
URL:            https://openprinting.github.io/cups/
VCS:            git:https://github.com/OpenPrinting/cups
#!RemoteAsset:  sha256:0339587204b4f9428dd0592eb301dec0bf9ea6ea8dce5d9690d56be585aba92d
Source0:        https://github.com/OpenPrinting/cups/releases/download/v%{version}/cups-%{version}-source.tar.gz
Source1:        macros.cups
BuildSystem:    autotools

BuildOption(conf):  --with-docdir=%{_datadir}/%{name}/www
BuildOption(conf):  --enable-debug
BuildOption(conf):  --disable-lspp
BuildOption(conf):  --enable-webif
BuildOption(conf):  --enable-relro
BuildOption(conf):  --enable-page-logging
BuildOption(conf):  --enable-sync-on-close
BuildOption(conf):  --with-exe-file-perm=0755
BuildOption(conf):  --with-cupsd-file-perm=0755
BuildOption(conf):  --with-log-file-perm=0600
BuildOption(conf):  --with-dbusdir=%{_sysconfdir}/dbus-1
BuildOption(conf):  --with-xinetd=no
BuildOption(conf):  --with-access-log-level=actions
BuildOption(conf):  --with-pkgconfpath=%{_libdir}/pkgconfig
BuildOption(conf):  --with-tls=gnutls
BuildOption(conf):  --with-rundir=%{_rundir}/cups
BuildOption(conf):  --localedir=%{_datadir}/locale

BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libacl)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(krb5)
BuildRequires:  systemd
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  automake
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  make
BuildRequires:  pkgconfig(pam)

Requires:       dbus
Requires:       systemd
Requires:       acl
%{?systemd_requires}
Requires(post): grep
Requires(post): sed

%patchlist
0001-cups-system-auth.patch
0002-cups-multilib.patch
0003-cups-banners.patch
0004-cups-direct-usb.patch
0005-cups-driverd-timeout.patch
0006-cups-usb-paperout.patch
0007-cups-uri-compat.patch
0008-cups-freebind.patch
0009-cups-ipp-multifile.patch
0010-cups-web-devices-timeout.patch
# https://github.com/OpenPrinting/cups/issues/1450
0011-cups-fix-check-logging-issue.patch

%description
CUPS is the standards-based, open source printing system developed by
Apple and OpenPrinting. It uses the Internet Printing Protocol (IPP)
to support printing to local and network printers.

%package        devel
Summary:        Development files for CUPS
License:        Apache-2.0
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(gnutls)
Requires:       pkgconfig(krb5)
Requires:       pkgconfig(zlib)
Requires:       pkgconfig

%description    devel
Development headers and pkgconfig files for CUPS. Install this package
if you want to build applications against libcups.

%conf -p
# regenerate autotools files
aclocal -I config-scripts
autoconf -f -I config-scripts

%install -a
# remove legacy init scripts
rm -rf %{buildroot}%{_initddir} %{buildroot}%{_sysconfdir}/{init.d,rc?.d}
install -d %{buildroot}%{_unitdir}

# compress PPDs
find %{buildroot}%{_datadir}/cups/model -name "*.ppd" | xargs gzip -n9f

# move binaries for alternatives system
pushd %{buildroot}%{_bindir}
for file in cancel lp lpq lpr lprm lpstat; do
    mv $file $file.cups
done
popd
mv %{buildroot}%{_sbindir}/lpc %{buildroot}%{_sbindir}/lpc.cups

# install macros
install -d %{buildroot}%{_datadir}/pixmaps %{buildroot}%{_rpmconfigdir}/macros.d
install -m 0644 %{SOURCE1} %{buildroot}%{_rpmconfigdir}/macros.d

# tmpfiles.d
install -d %{buildroot}%{_tmpfilesdir}
cat > %{buildroot}%{_tmpfilesdir}/cups.conf <<EOF
d /run/cups 0755 root lp -
d /run/cups/certs 0511 lp sys -
d /var/spool/cups/tmp - - - 30d
EOF

# %%find_lang --generate-subpackages doesn't work here.
find %{buildroot} -type f -o -type l | sed '
s:.*\('%{_datadir}'/\)\([^/_]\+\)\(.*\.po$\):%lang(\2) \1\2\3:
 /^%lang(C)/d
 /^\([^%].*\)/d
' > %{name}.lang

# Remove unshipped files.
rm -rf %{buildroot}%{_mandir}/cat? %{buildroot}%{_mandir}/*/cat?
rm -f %{buildroot}%{_datadir}/applications/cups.desktop
rm -rf %{buildroot}%{_datadir}/icons
rm -rf %{buildroot}%{_bindir}/cancel.cups
rm -rf %{buildroot}%{_bindir}/ippeveprinter
rm -rf %{buildroot}%{_bindir}/ipptool
rm -rf %{buildroot}%{_bindir}/lp.cups
rm -rf %{buildroot}%{_bindir}/lpoptions
rm -rf %{buildroot}%{_bindir}/lpq.cups
rm -rf %{buildroot}%{_bindir}/lpr.cups
rm -rf %{buildroot}%{_bindir}/lprm.cups
rm -rf %{buildroot}%{_bindir}/lpstat.cups
rm -rf %{buildroot}%{_unitdir}/cups-lpd.socket
rm -rf %{buildroot}%{_unitdir}/cups-lpd@.service
# there are pdf-banners shipped with cups-filters (#919489)
rm -rf %{buildroot}%{_datadir}/cups/banners
rm -f %{buildroot}%{_datadir}/cups/data/testprint

%files -f %{name}.lang
%license LICENSE NOTICE
%doc README.md CREDITS.md CHANGES.md
%{_bindir}/cupstestppd
%{_bindir}/ppd*
%{_sbindir}/*
%{_libdir}/libcups.so.2
%{_libdir}/libcupsimage.so.2
%{cups_serverbin}/daemon/*
%{cups_serverbin}/backend/*
%{cups_serverbin}/cgi-bin
%{cups_serverbin}/filter/*
%{cups_serverbin}/monitor
%{cups_serverbin}/notifier
%{cups_serverbin}/command/*
%{_datadir}/cups
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/cups.conf
%config(noreplace) %{_sysconfdir}/pam.d/cups
%{_tmpfilesdir}/cups.conf
%{_unitdir}/cups.service
%{_unitdir}/cups.socket
%{_unitdir}/cups.path
%{_mandir}/man?/*
%attr(0640,root,lp) %{_sysconfdir}/cups/cupsd.conf.default
%attr(0640,root,lp) %{_sysconfdir}/cups/cupsd.conf
%attr(0640,root,lp) %{_sysconfdir}/cups/cups-files.conf
%attr(0640,root,lp) %{_sysconfdir}/cups/cups-files.conf.default
%attr(0644,root,lp) %{_sysconfdir}/cups/snmp.conf
%attr(0640,root,lp) %{_sysconfdir}/cups/snmp.conf.default
%attr(0644, root, root) %{_unitdir}/system-cups.slice

%files devel
%{_bindir}/cups-config
%{_includedir}/cups
%{_libdir}/*.so
%{_libdir}/pkgconfig/cups.pc
%{_rpmconfigdir}/macros.d/macros.cups

%changelog
%autochangelog
