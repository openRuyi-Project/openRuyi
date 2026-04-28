# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: ayostl <yao_xp@yeah.net>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# If we want to enable building docs, change this to 1.
%bcond docs 0
# Same as above
%bcond selinux 1
%bcond nis 0
# We need to enable once systemd is available
# Also we need to add systemd %%install stuff maybe
%bcond systemd 1

Name:           pam
Version:        1.7.1
Release:        %autorelease
Summary:        An extensible library which provides authentication for applications
License:        BSD-3-Clause AND GPL-2.0-or-later
URL:            http://www.linux-pam.org/
VCS:            git:https://github.com/linux-pam/linux-pam
#!RemoteAsset:  sha256:21dbcec6e01dd578f14789eac9024a18941e6f2702a05cf91b28c232eeb26ab0
Source0:        https://github.com/linux-pam/linux-pam/releases/download/v%{version}/Linux-PAM-%{version}.tar.xz
#!RemoteAsset:  sha256:6971f4793e38f01c644de0da24f4ab2c2afb934b02b7c273fa1e53b859d36529
Source1:        https://github.com/linux-pam/linux-pam/releases/download/v%{version}/Linux-PAM-%{version}.tar.xz.asc
# Macros for us
Source2:        macros.pam
Source3:        pam.conf
# Other essential files
Source4:        other.pamd
Source5:        su.pamd
BuildSystem:    meson

# Backport upstream fixes
Patch0:         0001-post-v1.7.1.patch

# We need to tell rpm where to find various macros
%{load:%{SOURCE2}}

BuildOption(conf):  -Daudit=enabled

%if %{with systemd}
BuildOption(conf):  -Dlogind=enabled
%else
BuildOption(conf):  -Dlogind=disabled
%endif
BuildOption(conf):  -Delogind=disabled
BuildOption(conf):  -Dopenssl=enabled
BuildOption(conf):  -Dpam_userdb=enabled
BuildOption(conf):  -Ddb=gdbm
%if %{with selinux}
BuildOption(conf):  -Dselinux=enabled
%else
BuildOption(conf):  -Dselinux=disabled
%endif
%if %{with nis}
BuildOption(conf):  -Dnis=enabled
%else
BuildOption(conf):  -Dnis=disabled
%endif
%if %{with docs}
BuildOption(conf):  -Ddocs=enabled
%else
BuildOption(conf):  -Ddocs=disabled
%endif
BuildOption(conf):  -Dpwaccess=disabled

BuildRequires:  audit-devel
BuildRequires:  gdbm-devel
BuildRequires:  pkgconfig(libeconf)
%if %{with nis}
BuildRequires:  pkgconfig(libnsl)
%endif
%if %{with selinux}
BuildRequires:  pkgconfig(libselinux)
%endif
%if %{with systemd}
BuildRequires:  pkgconfig(systemd)
%endif
BuildRequires:  pkgconfig(libtirpc)
BuildRequires:  pkgconfig(libxcrypt)
BuildRequires:  meson
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig

Requires:       openruyi-authselect-profiles

%description
PAM (Pluggable Authentication Modules) is a system security tool that
allows system administrators to set authentication policy without
having to recompile programs that handle authentication.

%package        devel
Summary:        Files needed for developing PAM-aware applications and modules for PAM

%description    devel
PAM (Pluggable Authentication Modules) is a system security tool that
allows system administrators to set authentication policy without
having to recompile programs that handle authentication. This package
contains header files used for building both PAM-aware applications
and modules for use with the PAM system.

%if %{with docs}
%package        doc
Summary:        Extra documentation for PAM.
Requires:       pam = %{version}-%{release}
Provides:       pam-docs = %{version}-%{release}
BuildArch:      noarch
BuildRequires:  docbook5-schemas
BuildRequires:  docbook5-style-xsl
BuildRequires:  elinks
BuildRequires:  libxslt
BuildRequires:  linuxdoc-tools

%description    doc
PAM (Pluggable Authentication Modules) is a system security tool that
allows system administrators to set authentication policy without
having to recompile programs that handle authentication. The pam-doc
contains extra documentation for PAM. Currently, this includes additional
documentation in txt and html format.
%endif

%install -a
# Install the macros file
install -D -m 644 %{SOURCE2} %{buildroot}%{_rpmconfigdir}/macros.d/macros.%{name}

%if %{with selinux}
# Temporary compat link
ln -sf pam_sepermit.so %{buildroot}%{_pam_moduledir}/pam_selinux_permit.so
%endif

# RPM uses docs from source tree
rm -rf %{buildroot}%{_datadir}/doc/Linux-PAM

# Install default configuration files.
install -d -m 755 %{buildroot}%{_pam_confdir}
install -d -m 755 %{buildroot}%{_pam_vendordir}
install -m 644 %{SOURCE4} %{buildroot}%{_pam_confdir}/other
install -m 644 %{SOURCE5} %{buildroot}%{_pam_confdir}/su

for phase in auth acct passwd session ; do
  ln -sf pam_unix.so %{buildroot}%{_pam_moduledir}/pam_unix_${phase}.so
done

# Remove .la files and make new .so links -- this depends on the value
# of _libdir not changing, and *not* being /usr/lib.
for lib in libpam libpamc libpam_misc ; do
  rm -f %{buildroot}%{_pam_libdir}/${lib}.la
done
%if "%{_pam_libdir}" != "%{_libdir}"
install -d -m 755 %{buildroot}%{_libdir}
for lib in libpam libpamc libpam_misc ; do
  pushd %{buildroot}%{_libdir}
  ln -sf %{_pam_libdir}/${lib}.so.*.* ${lib}.so
  popd
  rm -f %{buildroot}%{_pam_libdir}/${lib}.so
done
%endif

# Duplicate doc file sets.
rm -fr %{buildroot}/usr/share/doc/pam

# Install the file for autocreation of /var/run subdirectories on boot
install -m644 -D %{SOURCE3} %{buildroot}%{_prefix}/lib/tmpfiles.d/pam.conf

# Install systemd unit file.
install -m644 -D %{_vpath_builddir}/modules/pam_namespace/pam_namespace.service \
  %{buildroot}%{_unitdir}/pam_namespace.service

# Fix other configuration files
install -d -m 755 %{buildroot}%{_pam_secconfdir}
for f in access.conf faillock.conf group.conf limits.conf namespace.conf pwhistory.conf time.conf pam_env.conf; do
  install -m 644 %{buildroot}%{_datadir}/pam/security/$f %{buildroot}%{_pam_secconfdir}/
done
# /etc/environment will be installed by the setup package
# install -m 644 %{buildroot}%{_datadir}/pam/environment %{buildroot}%{_sysconfdir}/environment
install -m 755 %{buildroot}%{_datadir}/pam/security/namespace.init %{buildroot}%{_pam_secconfdir}/
rm -rf %{buildroot}%{_datadir}/pam/security
rm -f  %{buildroot}%{_datadir}/pam/environment

%if %{with docs}
# Install doc files to unified location.
install -d -m 755 %{buildroot}%{_pkgdocdir}/{adg/html,mwg/html,sag/html}
install -p -m 644 doc/specs/rfc86.0.txt %{buildroot}%{_pkgdocdir}
for i in adg mwg sag; do
  install -p -m 644 %{_vpath_builddir}/doc/$i/*.txt %{buildroot}%{_pkgdocdir}/$i
  cp -pr %{_vpath_builddir}/doc/$i/html/* %{buildroot}%{_pkgdocdir}/$i/html
done
find %{buildroot}%{_pkgdocdir} -type d | xargs chmod 755
find %{buildroot}%{_pkgdocdir} -type f | xargs chmod 644
%endif

# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
%find_lang Linux-PAM --generate-subpackages

%files
%license Copyright
%dir %{_pam_confdir}
%dir %{_pam_vendordir}
%config(noreplace) %{_pam_confdir}/other
%config(noreplace) %{_pam_confdir}/su
%{_rpmconfigdir}/macros.d/macros.%{name}
%{_sbindir}/pam_namespace_helper
%{_sbindir}/faillock
#%{_sysconfdir}/environment
%attr(4755,root,root) %{_sbindir}/pam_timestamp_check
%attr(4755,root,shadow) %{_sbindir}/unix_chkpwd

%attr(0755,root,root) %{_sbindir}/mkhomedir_helper
%attr(0755,root,root) %{_sbindir}/pwhistory_helper
%{_pam_libdir}/libpam.so.0*
%{_pam_libdir}/libpamc.so.0*
%{_pam_libdir}/libpam_misc.so.0*
%dir %{_pam_moduledir}
%{_pam_moduledir}/pam_access.so
%{_pam_moduledir}/pam_canonicalize_user.so
%{_pam_moduledir}/pam_debug.so
%{_pam_moduledir}/pam_deny.so
%{_pam_moduledir}/pam_echo.so
%{_pam_moduledir}/pam_env.so
%{_pam_moduledir}/pam_exec.so
%{_pam_moduledir}/pam_faildelay.so
%{_pam_moduledir}/pam_faillock.so
%{_pam_moduledir}/pam_filter.so
%{_pam_moduledir}/pam_ftp.so
%{_pam_moduledir}/pam_group.so
%{_pam_moduledir}/pam_issue.so
%{_pam_moduledir}/pam_keyinit.so
%{_pam_moduledir}/pam_limits.so
%{_pam_moduledir}/pam_listfile.so
%{_pam_moduledir}/pam_localuser.so
%{_pam_moduledir}/pam_loginuid.so
%{_pam_moduledir}/pam_mail.so
%{_pam_moduledir}/pam_mkhomedir.so
%{_pam_moduledir}/pam_motd.so
%{_pam_moduledir}/pam_namespace.so
%{_pam_moduledir}/pam_nologin.so
%{_pam_moduledir}/pam_permit.so
%{_pam_moduledir}/pam_pwhistory.so
%{_pam_moduledir}/pam_rhosts.so
%{_pam_moduledir}/pam_rootok.so
%if %{with selinux}
%{_sbindir}/unix_update
%{_pam_moduledir}/pam_selinux.so
%{_pam_moduledir}/pam_selinux_permit.so
%{_pam_moduledir}/pam_sepermit.so
%endif
%{_pam_moduledir}/pam_securetty.so
%{_pam_moduledir}/pam_setquota.so
%{_pam_moduledir}/pam_shells.so
%{_pam_moduledir}/pam_stress.so
%{_pam_moduledir}/pam_succeed_if.so
%{_pam_moduledir}/pam_time.so
%{_pam_moduledir}/pam_timestamp.so
%{_pam_moduledir}/pam_tty_audit.so
%{_pam_moduledir}/pam_umask.so
%{_pam_moduledir}/pam_unix.so
%{_pam_moduledir}/pam_unix_acct.so
%{_pam_moduledir}/pam_unix_auth.so
%{_pam_moduledir}/pam_unix_passwd.so
%{_pam_moduledir}/pam_unix_session.so
%{_pam_moduledir}/pam_userdb.so
%{_pam_moduledir}/pam_usertype.so
%{_pam_moduledir}/pam_warn.so
%{_pam_moduledir}/pam_wheel.so
%{_pam_moduledir}/pam_xauth.so
%{_pam_moduledir}/pam_filter
%{_unitdir}/pam_namespace.service
%dir %{_pam_secconfdir}
%config(noreplace) %{_pam_secconfdir}/access.conf
%config(noreplace) %{_pam_secconfdir}/faillock.conf
%config(noreplace) %{_pam_secconfdir}/group.conf
%config(noreplace) %{_pam_secconfdir}/limits.conf
%dir %{_pam_secconfdir}/limits.d
%config(noreplace) %{_pam_secconfdir}/namespace.conf
%dir %{_pam_secconfdir}/namespace.d
%attr(755,root,root) %config(noreplace) %{_pam_secconfdir}/namespace.init
%config(noreplace) %{_pam_secconfdir}/pam_env.conf
%config(noreplace) %{_pam_secconfdir}/pwhistory.conf
%config(noreplace) %{_pam_secconfdir}/time.conf
%{_prefix}/lib/tmpfiles.d/pam.conf
%if %{with docs}
%{_mandir}/man5/*
%{_mandir}/man8/*
%endif

%files devel
#dir %{_pkgdocdir}
#doc %{_pkgdocdir}/rfc86.0.txt
%{_includedir}/security
%if %{with docs}
%{_mandir}/man3/*
%endif
%{_libdir}/libpam.so
%{_libdir}/libpamc.so
%{_libdir}/libpam_misc.so
%{_libdir}/pkgconfig/pam.pc
%{_libdir}/pkgconfig/pam_misc.pc
%{_libdir}/pkgconfig/pamc.pc

%if %{with docs}
%files doc
%doc %{_pkgdocdir}
%endif

%changelog
%autochangelog
