# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: laokz <zhangkai@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Originally extracted from openSUSE
# Authors: SUSE LLC and contributors

# Disable LTO due to a usage of top-level assembler that causes LTO issues
%global _lto_cflags %{nil}

%define __filter_GLIBC_PRIVATE 1

%define enable_stackguard_randomization 1

# We need to consider the nscd subpackage, or not.
%bcond nscd 1
# This is libnsl1, we already have newer libnsl - 251
%bcond libnsl 0

Name:           glibc
Summary:        Standard Shared Libraries (from the GNU C Library)
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-2.1-or-later WITH GCC-exception-2.0 AND GPL-3.0-or-later
Version:        2.43
Release:        %autorelease
URL:            https://www.gnu.org/software/libc/libc.html
#!RemoteAsset:  sha256:d9c86c6b5dbddb43a3e08270c5844fc5177d19442cf5b8df4be7c07cd5fa3831
Source0:        https://ftpmirror.gnu.org/gnu/glibc/glibc-%{version}.tar.xz
Source1:        nsswitch.conf
%if %{with nscd}
Source2:        nscd.tmpfiles
Source3:        nscd.service
Source4:        nscd.sysusers
%endif

# For obvious reasons.
Patch2000:      glibc-2.4-china.diff

BuildRequires:  pkgconfig(audit)
BuildRequires:  bison
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  texinfo
BuildRequires:  python3
BuildRequires:  systemd-rpm-macros
BuildRequires:  systemtap-sdt-devel
BuildRequires:  xz
BuildRequires:  pkgconfig(zlib)
# Provide Scrt1.o for _FORTIFY_SOURCE configure.
# TODO: how about bootstrap build? - 251
BuildRequires:  glibc-devel

Provides:       rtld(GNU_HASH)

Requires(pre):  filesystem

Recommends:     glibc-extra
Recommends:     glibc-gconv-modules-extra

%description
The GNU C Library provides the most important standard libraries used
by nearly all programs: the standard C library, the standard math
library, and the POSIX thread library. A system is not functional
without these libraries.

%package        devel
Summary:        Include Files and Libraries Mandatory for Development
License:        BSD-3-Clause AND LGPL-2.1-or-later AND LGPL-2.1-or-later WITH GCC-exception-2.0 AND GPL-2.0-or-later
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(libxcrypt)
Requires:       linux-headers

%description    devel
These libraries are needed to develop programs which use the standard C
library.

%package        utils
Summary:        Development utilities from the GNU C Library
License:        LGPL-2.1-or-later
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    utils
The glibc-utils package contains mtrace, a memory leak tracer and
xtrace, a function call tracer which can be helpful during program
debugging.

If you are unsure if you need this, do not install this package.

%package        doc
Summary:        Documentation for the GNU C Library
BuildArch:      noarch

%description    doc
This package contains the documentation for the GNU C library stored as
info files.

%package        locale-base
Summary:        en_US and zh_CN Locale Data for Localized Programs
License:        GPL-2.0-or-later AND MIT AND LGPL-2.1-or-later
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    locale-base
Locale data for the internationalisation features of the GNU C library.
This package contains the U.S. English and Simplified Chinese locales.

%package        locale
Summary:        Locale Data for Localized Programs
License:        GPL-2.0-or-later AND MIT AND LGPL-2.1-or-later
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    locale
Locale data for the internationalisation features of the GNU C library.

%package        gconv-modules-extra
Summary:        Non-essential gconv modules
License:        LGPL-2.1-or-later
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       glibc-locale-base:%{_libdir}/gconv/BIG5.so

%description    gconv-modules-extra
Modules for use by the iconv facility, to support encodings other than
Latin-1 and UTF based.

%package        static
Summary:        C library static libraries for -static linking
License:        BSD-3-Clause AND LGPL-2.1-or-later AND LGPL-2.1-or-later WITH GCC-exception-2.0 AND GPL-2.0-or-later
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(libxcrypt)

%description    static
The glibc-static package contains the C library static libraries
for -static linking.  You don't need these, unless you link statically,
which is highly discouraged.

%package        extra
# makedb requires libselinux. We add this program in a separate
# package so that glibc does not require libselinux.
Summary:        Extra binaries from GNU C Library
License:        LGPL-2.1-or-later
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    extra
The glibc-extra package contains some extra binaries for glibc that
are not essential but recommend for use.

makedb: A program to create a database for nss

%if %{with libnsl}
%package     -n libnsl
Summary:        Legacy Network Support Library (NIS)
License:        LGPL-2.1-or-later

%description -n libnsl
Network Support Library for legacy architectures.  This library does not
have support for IPv6.
%endif

%if %{with nscd}
%package     -n nscd
Summary:        Name Service Caching Daemon
License:        GPL-2.0-or-later
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires(pre):  systemd-sysusers
%{?systemd_requires}

%description -n nscd
Nscd caches name service lookups and can dramatically improve
performance with NIS, NIS+, and LDAP.
%endif

%prep
%autosetup -n glibc-%{version} -p1

%build
uname -a
uptime || :
ulimit -a
nice
# We do not want configure to figure out the system its building one
# to support a common ground and thus set build and host ourself.
target="%{_target_cpu}-openruyi-linux"
%define build %{_target_cpu}-openruyi-linux
# Default CFLAGS and Compiler
#
enable_stack_protector=
BuildFlags=
tmp="%{build_cflags}"
for opt in $tmp; do
  case $opt in
    -fstack-protector-*) enable_stack_protector=${opt#-fstack-protector-} ;;
    -fstack-protector) enable_stack_protector=yes ;;
    -D_FORTIFY_SOURCE=*) enable_fortify_source=${opt#-D_FORTIFY_SOURCE=} ;;
    -ffortify=* | *_FORTIFY_SOURCE*) ;;
    *) BuildFlags+=" $opt" ;;
  esac
done

#
# Build base glibc
#
mkdir build-%{_target_cpu}
cd build-%{_target_cpu}

../configure \
    CFLAGS="$BuildFlags" BUILD_CFLAGS="$BuildFlags" \
    CC="%__cc" CXX="%__cxx" \
    --prefix=%{_prefix} \
    --libexecdir=%{_libexecdir} \
    --infodir=%{_infodir} \
    --build=%{build} \
    --host=${target} \
    --enable-systemtap \
%if %{enable_stackguard_randomization}
    --enable-stackguard-randomization \
%endif
    ${enable_stack_protector:+--enable-stack-protector=$enable_stack_protector} \
    ${enable_fortify_source:+--enable-fortify-source=$enable_fortify_source} \
    --enable-tunables \
    --enable-kernel=4.15 \
    --with-bugurl=%{_vendor_bug_url} \
    --enable-bind-now \
    --disable-timezone-tools \
%if %{without nscd}
    --disable-build-nscd \
    --disable-nscd \
%endif
    --disable-crypt || \
  {
    rc=$?;
    echo "------- BEGIN config.log ------";
    %{__cat} config.log;
    echo "------- END config.log ------";
    exit $rc;
  }

%make_build
cd ..

%check
make %{?_smp_mflags} %{?make_output_sync} -C build-%{_target_cpu} check-abi
make %{?_smp_mflags} %{?make_output_sync} -C build-%{_target_cpu} test t=elf/check-localplt

%define rtldlib %{_lib}
# Each architecture has a different name for the dynamic linker:
%define rtld_name ld-linux.so.3
%ifarch riscv64
%define rtldlib lib
%define rtld_name ld-linux-riscv64-lp64d.so.1
%endif
%ifarch x86_64
%define rtld_name ld-linux-x86-64.so.2
%endif

%define rtlddir %{_prefix}/%{rtldlib}

%install
mkdir -p %{buildroot}%{_libdir}
ln -s %{buildroot}%{_libdir} %{buildroot}/%{_lib}
%if "%{rtldlib}" != "%{_lib}"
mkdir -p %{buildroot}%{rtlddir}
ln -s %{buildroot}%{rtlddir} %{buildroot}/%{rtldlib}
%endif
mkdir -p %{buildroot}%{_sbindir}
ln -s %{buildroot}%{_sbindir} %{buildroot}/sbin

%if "%{_sbindir}" == "%{_bindir}"
ln -s bin %{buildroot}/%{_prefix}/sbin
%endif

%ifarch riscv64
mkdir -p %{buildroot}%{_libdir}
ln -s . %{buildroot}%{_libdir}/lp64d
%endif

# Install base glibc
%make_install install_root=%{buildroot} -C build-%{_target_cpu}
cd build-%{_target_cpu}
make %{?_smp_mflags} %{?make_output_sync} install_root=%{buildroot} localedata/install-locale-files
cd ..

%find_lang libc --generate-subpackages

install -m 644 %{SOURCE1} %{buildroot}/etc/nsswitch.conf

%if %{with nscd}
cp nscd/nscd.conf %{buildroot}/etc
mkdir -p %{buildroot}/run/nscd
mkdir -p %{buildroot}/var/lib/nscd
%endif

#
# Create ld.so.conf
#
cat > %{buildroot}/etc/ld.so.conf <<EOF
%if "%{_lib}" != "lib"
/usr/local/%{_lib}
%endif
/usr/local/lib
include /etc/ld.so.conf.d/*.conf
# /lib64, /lib, /usr/lib64 and /usr/lib gets added
# automatically by ldconfig after parsing this file.
# So, they do not need to be listed.
EOF
# Add ldconfig cache directory for directory ownership
mkdir -p %{buildroot}/var/cache/ldconfig

# Don't look at ldd! We don't wish a /bin/sh requires
chmod 644 %{buildroot}%{_bindir}/ldd

rm -f %{buildroot}%{_sbindir}/sln

%if %{with nscd}
mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 644 %{SOURCE2} %{buildroot}%{_tmpfilesdir}/nscd.conf
mkdir -p %{buildroot}%{_unitdir}
install -m 644 %{SOURCE3} %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sysusersdir}
install -m 644 %{SOURCE4} %{buildroot}%{_sysusersdir}/nscd.conf
%endif

# Move getconf to %{_libexecdir}/getconf/ to avoid cross device link
mv %{buildroot}%{_bindir}/getconf %{buildroot}%{_libexecdir}/getconf/getconf
ln -s %{_libexecdir}/getconf/getconf %{buildroot}%{_bindir}/getconf

rm %{buildroot}/%{_lib}
%if "%{rtldlib}" != "%{_lib}"
rm %{buildroot}/%{rtldlib}
%endif
rm %{buildroot}/sbin
%if "%{_sbindir}" == "%{_bindir}"
rm %{buildroot}/%{_prefix}/sbin
%endif

%if %{without libnsl}
rm -f %{buildroot}%{_libdir}/libnsl.so.1
%endif

%post -p <lua>
if posix.access("%{_sbindir}/ldconfig", "x") then
  rpm.spawn({ "%{_sbindir}/ldconfig", "-X" })
end

if posix.access("%{_sbindir}/iconvconfig", "x") and posix.access("%{_libdir}/gconv", "r") then
  rpm.spawn({
    "%{_sbindir}/iconvconfig",
    "-o", "%{_libdir}/gconv/gconv-modules.cache",
    "--nostdlib", "%{_libdir}/gconv"
  })
end

%postun -p %{_sbindir}/ldconfig

%post gconv-modules-extra -p <lua>
if posix.access("%{_sbindir}/iconvconfig", "x") and posix.access("%{_libdir}/gconv", "r") then
  rpm.spawn({
    "%{_sbindir}/iconvconfig",
    "-o", "%{_libdir}/gconv/gconv-modules.cache",
    "--nostdlib", "%{_libdir}/gconv"
  })
end

%postun gconv-modules-extra -p <lua>
if posix.access("%{_sbindir}/iconvconfig", "x") and posix.access("%{_libdir}/gconv", "r") then
  rpm.spawn({
    "%{_sbindir}/iconvconfig",
    "-o", "%{_libdir}/gconv/gconv-modules.cache",
    "--nostdlib", "%{_libdir}/gconv"
  })
end

%if %{with nscd}
%pre -n nscd
%sysusers_create_package nscd %{SOURCE4}

%preun -n nscd
%systemd_preun nscd.service

%post -n nscd
%systemd_post nscd.service

%postun -n nscd
%systemd_postun nscd.service
%endif

# Run ldconfig once per transaction when files are added to or removed from
# standard library paths or ld.so.conf.d.

%transfiletriggerin -P 2000000 -p <lua> -- /lib /usr/lib /lib64 /usr/lib64 /etc/ld.so.conf.d
rpm.spawn({"%{_sbindir}/ldconfig"})
%end

%transfiletriggerpostun -P 2000000 -p <lua> -- /lib /usr/lib /lib64 /usr/lib64 /etc/ld.so.conf.d
rpm.spawn({"%{_sbindir}/ldconfig"})
%end

%files -f libc.lang
# glibc
%defattr(-,root,root)
%license LICENSES
%config(noreplace) /etc/ld.so.conf
%attr(0644,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /etc/ld.so.cache
%config(noreplace) /etc/rpc
%verify(not md5 size mtime) %config(noreplace) /etc/nsswitch.conf
%attr(0644,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /etc/gai.conf
%doc posix/gai.conf
%{_bindir}/ld.so
%attr(755,root,root) %{rtlddir}/%{rtld_name}
%if 0%{?rtld_oldname:1}
%attr(755,root,root) %{rtlddir}/%{rtld_oldname}
%endif
%ifarch riscv64
%{_libdir}/lp64d
%endif
%{_libdir}/libBrokenLocale.so.1
%{_libdir}/libanl.so.1
%{_libdir}/libc.so.6*
%{_libdir}/libc_malloc_debug.so.0
%{_libdir}/libdl.so.2*
%{_libdir}/libm.so.6*
%{_libdir}/libnss_compat.so.2
%{_libdir}/libnss_db.so.2
%{_libdir}/libnss_dns.so.2
%{_libdir}/libnss_files.so.2
%{_libdir}/libnss_hesiod.so.2
%{_libdir}/libpthread.so.0
%{_libdir}/libresolv.so.2
%{_libdir}/librt.so.1
%{_libdir}/libthread_db.so.1
%{_libdir}/libutil.so.1
%ifarch x86_64
%{_libdir}/libmvec.so.1
%endif
%dir %attr(0700,root,root) /var/cache/ldconfig
%{_sbindir}/ldconfig
%{_bindir}/gencat
%{_bindir}/getconf
%{_bindir}/getent
%{_bindir}/iconv
%attr(755,root,root) %{_bindir}/ldd
%{_bindir}/locale
%{_bindir}/localedef
%dir %attr(0755,root,root) %{_libexecdir}/getconf
%{_libexecdir}/getconf/*
%{_sbindir}/iconvconfig
%dir %{_libdir}/gconv
%{_libdir}/gconv/ANSI_X3.110.so
%{_libdir}/gconv/CP1252.so
%{_libdir}/gconv/ISO8859-1.so
%{_libdir}/gconv/ISO8859-15.so
%{_libdir}/gconv/UNICODE.so
%{_libdir}/gconv/UTF-16.so
%{_libdir}/gconv/UTF-32.so
%{_libdir}/gconv/UTF-7.so
%{_libdir}/gconv/gconv-modules
%dir %{_libdir}/gconv/gconv-modules.d
%attr(0644,root,root) %verify(not md5 size mtime) %ghost %{_libdir}/gconv/gconv-modules.cache

%files devel
%defattr(-,root,root)
%license COPYING.LIB
%doc NEWS README
%{_bindir}/sprof
%{_includedir}/*
%{_libdir}/*.o
%{_libdir}/libBrokenLocale.so
%{_libdir}/libanl.so
%{_libdir}/libc.so
%{_libdir}/libc_malloc_debug.so
%{_libdir}/libm.so
%{_libdir}/libnss_compat.so
%{_libdir}/libnss_db.so
%{_libdir}/libnss_hesiod.so
%{_libdir}/libresolv.so
%{_libdir}/libthread_db.so
%ifarch x86_64
%{_libdir}/libmvec.so
%endif
# These static libraries are needed even for shared builds
%{_libdir}/libc_nonshared.a
%{_libdir}/libdl.a
%{_libdir}/libg.a
%{_libdir}/libmcheck.a
%{_libdir}/libpthread.a
%{_libdir}/librt.a
%{_libdir}/libutil.a

%files utils
%defattr(-,root,root)
%{_libdir}/libmemusage.so
%{_libdir}/libpcprofile.so
%dir %{_libdir}/audit
%{_libdir}/audit/sotruss-lib.so
%{_bindir}/mtrace
%{_bindir}/pcprofiledump
%{_bindir}/sotruss
%{_bindir}/xtrace
%{_bindir}/pldd

%files doc
%defattr(-,root,root)
%doc %{_infodir}/libc.info.gz
%doc %{_infodir}/libc.info-?.gz
%doc %{_infodir}/libc.info-??.gz

%files locale-base
%defattr(-,root,root)
%{_datadir}/locale/locale.alias
%dir %{_prefix}/lib/locale
%{_prefix}/lib/locale/C.utf8
%{_prefix}/lib/locale/en_US.utf8
%{_prefix}/lib/locale/zh_CN.utf8

%files locale
%defattr(-,root,root)
%{_prefix}/lib/locale
%{_prefix}/share/i18n
%exclude %{_prefix}/lib/locale/C.utf8
%exclude %{_prefix}/lib/locale/en_US.utf8
%exclude %{_prefix}/lib/locale/zh_CN.utf8

%files gconv-modules-extra
%dir %{_libdir}/gconv
%dir %{_libdir}/gconv/gconv-modules.d
%{_libdir}/gconv/gconv-modules.d/*.conf
%{_libdir}/gconv/*.so
%exclude %{_libdir}/gconv/ANSI_X3.110.so
%exclude %{_libdir}/gconv/CP1252.so
%exclude %{_libdir}/gconv/ISO8859-1.so
%exclude %{_libdir}/gconv/ISO8859-15.so
%exclude %{_libdir}/gconv/UNICODE.so
%exclude %{_libdir}/gconv/UTF-16.so
%exclude %{_libdir}/gconv/UTF-32.so
%exclude %{_libdir}/gconv/UTF-7.so

%files static
%defattr(-,root,root)
%{_libdir}/libBrokenLocale.a
%{_libdir}/libanl.a
%{_libdir}/libc.a
%{_libdir}/libm.a
%{_libdir}/libresolv.a
%ifarch x86_64
%{_libdir}/libm-%{version}.a
%{_libdir}/libmvec.a
%endif

%files extra
%defattr(-,root,root)
%{_bindir}/makedb
/var/db/Makefile

%if %{with libnsl}
%files -n libnsl
%{_libdir}/libnsl.so.1
%endif

%if %{with nscd}
%files -n nscd
%defattr(-,root,root)
%config(noreplace) /etc/nscd.conf
%{_sbindir}/nscd
%{_prefix}/lib/systemd/system/nscd.service
%dir %{_prefix}/lib/tmpfiles.d
%{_prefix}/lib/tmpfiles.d/nscd.conf
%dir %{_prefix}/lib/sysusers.d
%{_prefix}/lib/sysusers.d/nscd.conf
%dir %attr(0755,root,root) %ghost /run/nscd
%attr(0644,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /run/nscd/nscd.pid
%attr(0666,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /run/nscd/socket
%dir %attr(0755,root,root) /var/lib/nscd
%attr(0600,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /var/lib/nscd/passwd
%attr(0600,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /var/lib/nscd/group
%attr(0600,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /var/lib/nscd/hosts
%attr(0600,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /var/lib/nscd/services
%attr(0600,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /var/lib/nscd/netgroup
%endif

%changelog
%{?autochangelog}
