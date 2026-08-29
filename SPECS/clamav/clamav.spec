# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond milter 0

Name:           clamav
Version:        1.5.2
Release:        %autorelease
Summary:        End-user tools for the Clam Antivirus scanner
License:        MPL-2.0
URL:            https://www.clamav.net
VCS:            git:https://github.com/Cisco-Talos/clamav
#!RemoteAsset:  sha256:f34018cf22f05bdd9d1a1574ca07193e3e030ca52050c3e5c220e23a32314965
Source0:        https://www.clamav.net/downloads/production/%{name}-%{version}.tar.gz
Source1:        clamav.sysusers
Source2:        clamav.tmpfiles
Source3:        clamd.service
Source4:        freshclam.service
Source5:        freshclam.timer
Source6:        clamonacc.service
%if %{with milter}
# TODO: Add clamav-milter.service here.
%endif
BuildSystem:    cmake

BuildOption(conf):  -DENABLE_UNRAR=OFF
BuildOption(conf):  -DAPP_CONFIG_DIRECTORY=%{_sysconfdir}/clamav
BuildOption(conf):  -DDATABASE_DIRECTORY=%{_sharedstatedir}/clamav
BuildOption(conf):  -DCLAMAV_USER=vscan
BuildOption(conf):  -DCLAMAV_GROUP=vscan
BuildOption(conf):  -DENABLE_EXTERNAL_MSPACK=ON
BuildOption(conf):  -DENABLE_CLAMONACC=ON
BuildOption(conf):  -DSYSTEMD_UNIT_DIR=%{_unitdir}
%if %{with milter}
BuildOption(conf):  -DENABLE_MILTER=ON
%else
BuildOption(conf):  -DENABLE_MILTER=OFF
%endif

BuildRequires:  cmake
BuildRequires:  gettext-devel
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  systemd-rpm-macros
BuildRequires:  python3
BuildRequires:  python3dist(pytest)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libmspack)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)
%if %{with milter}
# TODO: Add milter BuildRequires here.
%endif

%patchlist
# Fixes libclamav pkg-config / clamav-config metadata - from fedora
2000-fix-libclamav-metadata.patch
# Fixes printf-style format specifiers and improves
# portability across architectures and ABIs - from openSUSE
2001-fixes-printf-style-format-specifiers.patch
# Update config
# TODO: When enable milter please update
2002-Change-upstream-sample-config-to-openRuyi-config.patch

%description
ClamAV is an anti-virus toolkit for detecting trojans, viruses,
malware, and other malicious threats. It provides a command line
scanner, a multi-threaded scanning daemon, and a tool for automatic
signature updates.

%package        libs
Summary:        Runtime libraries for ClamAV

%description    libs
This package contains the shared libraries used by ClamAV and by
applications linked against libclamav.

%package        devel
Summary:        Development files for ClamAV
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(openssl)

%description    devel
This package contains headerfiles and libraries which are needed to
build applications using clamav.

%prep -a
# We don't know if this is a good idea.
rm -rf libclamunrar
# But Keep the directory harmlessly present
# if upstream build scripts still reference it
mkdir -p libclamunrar

%install -a
install -d -m 0755 %{buildroot}%{_sharedstatedir}/clamav

# Turn sample configs into real config files.
for f in clamd freshclam; do
    if [ -f %{buildroot}%{_sysconfdir}/clamav/${f}.conf.sample ]; then
        mv %{buildroot}%{_sysconfdir}/clamav/${f}.conf.sample \
           %{buildroot}%{_sysconfdir}/clamav/${f}.conf
    fi
done

%if %{with milter}
if [ -f %{buildroot}%{_sysconfdir}/clamav/clamav-milter.conf.sample ]; then
    mv %{buildroot}%{_sysconfdir}/clamav/clamav-milter.conf.sample \
       %{buildroot}%{_sysconfdir}/clamav/clamav-milter.conf
fi
%else
rm -f %{buildroot}%{_sysconfdir}/clamav/clamav-milter.conf
rm -f %{buildroot}%{_sysconfdir}/clamav/clamav-milter.conf.sample
%endif

install -D -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/clamav.conf
install -D -m 0644 %{SOURCE2} %{buildroot}%{_tmpfilesdir}/clamav.conf

# Prefer our simpler single-instance services.
rm -f %{buildroot}%{_unitdir}/clamav-*.service
rm -f %{buildroot}%{_unitdir}/clamav-*.timer
rm -f %{buildroot}%{_unitdir}/clamav-daemon.*

install -D -m 0644 %{SOURCE3} %{buildroot}%{_unitdir}/clamd.service
install -D -m 0644 %{SOURCE4} %{buildroot}%{_unitdir}/freshclam.service
install -D -m 0644 %{SOURCE5} %{buildroot}%{_unitdir}/freshclam.timer
install -D -m 0644 %{SOURCE6} %{buildroot}%{_unitdir}/clamonacc.service
%if ! %{with milter}
rm -f %{buildroot}%{_sbindir}/clamav-milter
rm -f %{buildroot}%{_mandir}/man5/clamav-milter.conf.5*
rm -f %{buildroot}%{_mandir}/man8/clamav-milter.8*
rm -f %{buildroot}%{_unitdir}/clamav-milter.service
%endif

%pre
%sysusers_create_package %{name} %{SOURCE1}

%post
%tmpfiles_create_package %{name} %{SOURCE2}
%systemd_post clamd.service freshclam.timer clamonacc.service

%preun
%systemd_preun clamd.service freshclam.timer clamonacc.service

%postun
%systemd_postun_with_restart clamd.service clamonacc.service
%systemd_postun freshclam.timer

%files
%doc NEWS.md README.md
%doc %{_docdir}/ClamAV
%license COPYING*
%config(noreplace) %{_sysconfdir}/clamav/clamd.conf
%config(noreplace) %{_sysconfdir}/clamav/freshclam.conf
%{_bindir}/clambc
%{_bindir}/clamconf
%{_bindir}/clamdscan
%{_bindir}/clamdtop
%{_bindir}/clamscan
%{_bindir}/clamsubmit
%{_bindir}/freshclam
%{_bindir}/sigtool
%{_sbindir}/clamd
%{_sbindir}/clamonacc
%{_mandir}/man1/*
%{_mandir}/man5/clamd.conf.5*
%{_mandir}/man5/freshclam.conf.5*
%{_mandir}/man8/clamd.8*
%{_mandir}/man8/clamonacc.8*
%{_unitdir}/clamd.service
%{_unitdir}/freshclam.service
%{_unitdir}/freshclam.timer
%{_unitdir}/clamonacc.service
%{_sysusersdir}/clamav.conf
%{_tmpfilesdir}/clamav.conf
%{_sysconfdir}/clamav/certs/clamav.crt
%dir %attr(0755,vscan,vscan) %{_sharedstatedir}/clamav
%ghost %attr(0644,vscan,vscan) %{_sharedstatedir}/clamav/main.cvd
%ghost %attr(0644,vscan,vscan) %{_sharedstatedir}/clamav/main.cld
%ghost %attr(0644,vscan,vscan) %{_sharedstatedir}/clamav/daily.cvd
%ghost %attr(0644,vscan,vscan) %{_sharedstatedir}/clamav/daily.cld
%ghost %attr(0644,vscan,vscan) %{_sharedstatedir}/clamav/bytecode.cvd
%ghost %attr(0644,vscan,vscan) %{_sharedstatedir}/clamav/bytecode.cld
%ghost %attr(0644,vscan,vscan) %{_sharedstatedir}/clamav/freshclam.dat
%if %{with milter}
%config(noreplace) %{_sysconfdir}/clamav/clamav-milter.conf
%{_sbindir}/clamav-milter
%{_mandir}/man5/clamav-milter.conf.5*
%{_mandir}/man8/clamav-milter.8*
%{_unitdir}/clamav-milter.service
%endif

%files libs
%license COPYING*
%{_libdir}/libclamav.so.*
%{_libdir}/libfreshclam.so.*

%files devel
%{_includedir}/*
%{_libdir}/pkgconfig/libclamav.pc
%{_libdir}/libclamav.so
%{_libdir}/libfreshclam.so
%{_libdir}/libclamav_rust.a
%{_bindir}/clamav-config

%changelog
%autochangelog
