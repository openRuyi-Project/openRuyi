# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Dingli Zhang <dingli@iscas.ac.cn>
# SPDX-FileContributor: Jingkun Zheng <zhengjingkun@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global cups_serverbin %{_exec_prefix}/lib/cups
%global _test_target unittests

Name:           cups
Version:        2.4.20
Release:        %autorelease
Summary:        Standards-based, open source printing system for Linux
License:        Apache-2.0
URL:            https://openprinting.github.io/cups/
VCS:            git:https://github.com/OpenPrinting/cups
#!RemoteAsset:  sha256:ab4d9cd7f3e58060091d2b24972223d6401675f11c49b65abf4f6ef31dea22ff
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
BuildOption(conf):  --with-dnssd=avahi
BuildOption(conf):  --with-tls=gnutls
BuildOption(conf):  --with-rundir=%{_rundir}/cups
BuildOption(conf):  --localedir=%{_datadir}/locale

BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(avahi-client)
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
# https://github.com/OpenPrinting/cups/commit/6c61d23f5523055ec4374465e85d1dec9396994f
1000-Don-t-allow-clients-to-hold-a-job-open-longer-than-the-multiple-.patch
# https://github.com/OpenPrinting/cups/commit/7683948211d2ae36a1bc5bd1eab091ca389801ea
1001-Increase-size-of-supply-level-name-buffer-GHSA-g863-fq3c-86jm.patch
# https://github.com/OpenPrinting/cups/commit/1ce8bb41d3d39241d7d37f3f8482cb582de8110b
1002-Increase-space-reservation-to-27-characters-for-resolution-value.patch
# https://github.com/OpenPrinting/cups/commit/d98a2face6390f88173ceec13e60603effe19530
1003-Range-limit-supply-level-values-to-avoid-buffer-overflow-GHSA-5c.patch
# https://github.com/OpenPrinting/cups/commit/4f79650387c5e1fed0573b7b1c549815c82df726
1004-Only-do-local-authentication-over-the-default-domain-socket-GHSA.patch
# https://github.com/OpenPrinting/cups/commit/bfdee59c7301a1722fbebf9a4fc87a9816f02324
1005-Update-the-random-number-generator-used-for-local-certificates-G.patch
# https://github.com/OpenPrinting/cups/commit/66dcc00b520f589324e27489958410c6aeb4cdeb
1006-Improve-validation-of-subscription-attributes-GHSA-p6cf-j6h3-rcf.patch
# https://github.com/OpenPrinting/cups/commit/b52b85906fd889ad3859b0dfcacc9235f5681b44
1007-Fix-octetString-check-in-get_options.patch
# https://github.com/OpenPrinting/cups/commit/441cda8da54f3da81850865014fb388fc8a622b8
1008-Protect-against-Foomatic-driver-vulnerabilities-GHSA-w5p3-jrq8-w.patch
# https://github.com/OpenPrinting/cups/commit/0beeb4e78730ab11e975d19eaf6bb53679ec6086
1009-Validate-printer-server-responses-GHSA-hp44-ph36-rc52.patch
# https://github.com/OpenPrinting/cups/commit/25d68309b1af89c4b003f27f56ab0f8e7a189ea3
1010-Add-JobTicketComments-directive-fix-job-ticket-comment-support-a.patch
# https://github.com/OpenPrinting/cups/commit/5d44355084c3efdcdd8729eab65f18635adf6a0c
1011-Don-t-use-bool-type-in-2.4.x-code.patch
# https://github.com/OpenPrinting/cups/commit/b268a155d0ce1c1d88b76c758c874cbf1bea1a13
1012-Make-sure-that-supply-level-names-do-not-contain-newlines-Issue-.patch
# https://github.com/OpenPrinting/cups/commit/a7a0f4fd4497180aed601836a3159f9f79e4375f
1013-Fix-build-error.patch
# https://github.com/OpenPrinting/cups/commit/e195881f4a7179c0caf79a1212894f877b19963c
1014-Update-list-of-read-only-job-attributes-GHSA-3mc2-9qgx-j5rx.patch
# https://github.com/OpenPrinting/cups/commit/586fbabcf6603bce630fdf34cfa9e53eddd89019
1015-Don-t-allow-printer-MIME-media-types-for-print-jobs-GHSA-fw5x-gq.patch

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
d /run/cups/certs 0511 nobody sys -
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
%doc README.md CREDITS.md CHANGES.md
%license LICENSE NOTICE
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
