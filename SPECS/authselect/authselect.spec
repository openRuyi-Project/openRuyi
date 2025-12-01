# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:          authselect
Version:       1.6.1
Release:       %autorelease
Summary:       A tool to select system authentication and identity sources
License:       GPL-3.0-or-later
URL:           https://github.com/authselect/authselect
#!RemoteAsset
Source:        https://github.com/authselect/authselect/archive/%{version}/authselect-%{version}.tar.gz
BuildSystem:   autotools

BuildOption(conf): --disable-rpath
BuildOption(conf): --disable-static
BuildOption(conf): --with-completion-dir=%{bash_completions_dir}
BuildOption(conf): --with-pythonbin=%{__python3}
BuildOption(conf): --disable-nls

BuildRequires: autoconf automake libtool popt-devel cmocka-devel
BuildRequires: m4  python3-devel libselinux-devel chrpath
Requires:      grep sed systemd gawk coreutils findutils pam >= 1.3.1
Requires:      libpwquality
%description
Authselect is a tool to configure system authentication and identity sources
from a list of supported profiles. It replaces the legacy authconfig tool.

%package       devel
Summary:       Development files for the authselect library
Requires:      %{name} = %{version}

%description   devel
This package contains the development library files and headers for the
authselect tool, used for developing front-ends.


%conf -p
autoreconf -ivf

%install -a
# fix error  0001: file '/usr/bin/authselect' contains a standard runpath '/usr/lib64' in [/usr/lib64]
chrpath -d %{buildroot}%{_bindir}/authselect

find %{buildroot} -type f -name "*.la" -delete -print
rm -fr %{buildroot}%{_datadir}/doc/%{name}

%preun
# This script must be executed before any files are removed.
if [ $1 == 0 ] ; then
    # Remove authselect symbolic links so all authselect files can be
    # deleted safely. If this fail, the uninstallation must fail to avoid
    # breaking the system by removing PAM files. However, the command can
    # only fail if it can not write to the file system.
    %{_bindir}/authselect opt-out || exit 1
fi

%posttrans
# If this is a new installation select the default configuration.
if [ $1 == 1 ] ; then
    %{_bindir}/authselect select local --force --nobackup &> /dev/null
    exit 0
fi
# Apply any changes to profiles (validates configuration first internally)
%{_bindir}/authselect apply-changes &> /dev/null
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

%files devel
%{_includedir}/authselect.h
%{_libdir}/libauthselect.so
%{_libdir}/pkgconfig/authselect.pc

%changelog
%{?autochangelog}
