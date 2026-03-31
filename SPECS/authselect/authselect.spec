# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           authselect
Version:        1.6.1
Release:        %autorelease
Summary:        A tool to select system authentication and identity sources
License:        GPL-3.0-or-later
URL:            https://github.com/authselect/authselect
#!RemoteAsset
Source0:        https://github.com/authselect/authselect/archive/%{version}/authselect-%{version}.tar.gz
Source1:        openruyi-local-README
Source2:        openruyi-local-REQUIREMENTS
Source3:        openruyi-local-dconf-db
Source4:        openruyi-local-dconf-locks
Source5:        openruyi-local-fingerprint-auth
Source6:        openruyi-local-nsswitch.conf
Source7:        openruyi-local-password-auth
Source8:        openruyi-local-postlogin
Source9:        openruyi-local-smartcard-auth
Source10:       openruyi-local-system-auth
BuildSystem:    autotools

BuildOption(conf):  --disable-rpath
BuildOption(conf):  --disable-static
BuildOption(conf):  --with-completion-dir=%{bash_completions_dir}
BuildOption(conf):  --with-pythonbin=%{__python3}
BuildOption(conf):  --disable-nls

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(popt)
BuildRequires:  pkgconfig(cmocka)
BuildRequires:  m4
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  chrpath

Requires:       grep
Requires:       sed
Requires:       systemd
Requires:       gawk
Requires:       coreutils
Requires:       findutils
Requires:       pam
Requires:       libpwquality

%description
Authselect is a tool to configure system authentication and identity sources
from a list of supported profiles. It replaces the legacy authconfig tool.

%package        -n openruyi-authselect-profiles
Summary:        openRuyi vendor authselect profiles
Requires:       authselect = %{version}-%{release}
BuildArch:      noarch

%description    -n openruyi-authselect-profiles
This package ships the vendor-owned authselect profiles used by openRuyi.
It provides the openruyi-local base profile under
/usr/share/authselect/vendor and keeps the distro authentication policy
separate from the authselect tool itself.

%package        devel
Summary:        Development files for the authselect library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the development library files and headers for the
authselect tool, used for developing front-ends.

%conf -p
autoreconf -ivf

%install -a
# fix error  0001: file '/usr/bin/authselect' contains a standard runpath '/usr/lib64' in [/usr/lib64]
chrpath -d %{buildroot}%{_bindir}/authselect

rm -fr %{buildroot}%{_datadir}/doc/%{name}

install -d -m 0755 %{buildroot}%{_datadir}/authselect/vendor/openruyi-local
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/authselect/vendor/openruyi-local/README
install -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/authselect/vendor/openruyi-local/REQUIREMENTS
install -m 0644 %{SOURCE3} %{buildroot}%{_datadir}/authselect/vendor/openruyi-local/dconf-db
install -m 0644 %{SOURCE4} %{buildroot}%{_datadir}/authselect/vendor/openruyi-local/dconf-locks
install -m 0644 %{SOURCE5} %{buildroot}%{_datadir}/authselect/vendor/openruyi-local/fingerprint-auth
install -m 0644 %{SOURCE6} %{buildroot}%{_datadir}/authselect/vendor/openruyi-local/nsswitch.conf
install -m 0644 %{SOURCE7} %{buildroot}%{_datadir}/authselect/vendor/openruyi-local/password-auth
install -m 0644 %{SOURCE8} %{buildroot}%{_datadir}/authselect/vendor/openruyi-local/postlogin
install -m 0644 %{SOURCE9} %{buildroot}%{_datadir}/authselect/vendor/openruyi-local/smartcard-auth
install -m 0644 %{SOURCE10} %{buildroot}%{_datadir}/authselect/vendor/openruyi-local/system-auth

%preun
# This script must be executed before any files are removed.
if [ $1 == 0 ] ; then
    # Remove authselect symbolic links so all authselect files can be
    # deleted safely. If this fail, the uninstallation must fail to avoid
    # breaking the system by removing PAM files. However, the command can
    # only fail if it can not write to the file system.
    %{_bindir}/authselect opt-out || exit 1
fi

%preun -n openruyi-authselect-profiles
if [ $1 == 0 ] ; then
    current_profile="$("%{_bindir}/authselect" current --raw 2>/dev/null || :)"
    case "$current_profile" in
        openruyi-*)
            %{_bindir}/authselect opt-out || exit 1
            ;;
    esac
fi

%posttrans -n openruyi-authselect-profiles
current_profile="$("%{_bindir}/authselect" current --raw 2>/dev/null || :)"

case "$current_profile" in
    ""|local|local\ *)
        # Fresh system or legacy default profile: migrate to distro-owned profile
        %{_bindir}/authselect select openruyi-local --force --nobackup >/dev/null 2>&1 || :
        ;;
    openruyi-* )
        # Already on an openRuyi-owned profile: regenerate managed files
        %{_bindir}/authselect apply-changes >/dev/null 2>&1 || :
        ;;
    * )
        # sssd / winbind / custom profile: do not override user choice
        :
        ;;
esac

exit 0

%files
%license COPYING
%doc README.md
%dir %{_sysconfdir}/authselect
%dir %{_sysconfdir}/authselect/custom
%ghost %attr(0644,root,root) %{_sysconfdir}/authselect/authselect.conf
%ghost %attr(0644,root,root) %{_sysconfdir}/authselect/dconf-db
%ghost %attr(0644,root,root) %{_sysconfdir}/authselect/dconf-locks
%ghost %attr(0644,root,root) %{_sysconfdir}/authselect/fingerprint-auth
%ghost %attr(0644,root,root) %{_sysconfdir}/authselect/nsswitch.conf
%ghost %attr(0644,root,root) %{_sysconfdir}/authselect/password-auth
%ghost %attr(0644,root,root) %{_sysconfdir}/authselect/postlogin
%ghost %attr(0644,root,root) %{_sysconfdir}/authselect/smartcard-auth
%ghost %attr(0644,root,root) %{_sysconfdir}/authselect/system-auth
%ghost %attr(0644,root,root) %{_sysconfdir}/nsswitch.conf
%ghost %attr(0644,root,root) %{_sysconfdir}/pam.d/fingerprint-auth
%ghost %attr(0644,root,root) %{_sysconfdir}/pam.d/password-auth
%ghost %attr(0644,root,root) %{_sysconfdir}/pam.d/postlogin
%ghost %attr(0644,root,root) %{_sysconfdir}/pam.d/smartcard-auth
%ghost %attr(0644,root,root) %{_sysconfdir}/pam.d/system-auth
%dir %{_localstatedir}/lib/authselect
%ghost %attr(0755,root,root) %{_localstatedir}/lib/authselect/backups/
%dir %{_datadir}/authselect
%dir %{_datadir}/authselect/vendor
%dir %{_datadir}/authselect/default
%{_datadir}/authselect/default/*
%{_bindir}/authselect
%{_libdir}/libauthselect.so.*

%files -n openruyi-authselect-profiles
%dir %{_datadir}/authselect/vendor/openruyi-local
%{_datadir}/authselect/vendor/openruyi-local/*

%files devel
%{_includedir}/authselect.h
%{_libdir}/libauthselect.so
%{_libdir}/pkgconfig/authselect.pc

%changelog
%{?autochangelog}
