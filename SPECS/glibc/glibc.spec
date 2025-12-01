# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: laokz <zhangkai@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Run with --with=fast_build to have a shorter turnaround
# It will avoid building some parts of glibc
%bcond_with    fast_build

%define flavor @BUILD_FLAVOR@%{nil}

%bcond build_all 0
%define build_main 1
%define build_utils %{with build_all}
%define build_testsuite %{with build_all}
%if "%flavor" == "utils"
%define build_main 0
%define build_utils 1
%define build_testsuite 0
%endif
%if "%flavor" == "testsuite"
%define build_main 0
%define build_utils 0
%define build_testsuite 1
%endif
%define host_arch %{_target_cpu}

%if %{build_main}
%define name_suffix %{nil}
%else
%define name_suffix -%{flavor}-src
%endif

%define __filter_GLIBC_PRIVATE 1
%if %{with fast_build} || %{build_utils} && %{without build_all}
%else
%endif

%define build_variants %{build_main}

%define disable_assert 0
%define enable_stackguard_randomization 1

%global glibc_post_funcs %{expand:
-- We use lua because there may be no shell that we can run during
-- glibc upgrade. We used to implement much of %%post as a C program,
-- but from an overall maintenance perspective the lua in the spec
-- file was simpler and safer given the operations required.
-- All lua code will be ignored by rpm-ostree; see:
-- https://github.com/projectatomic/rpm-ostree/pull/1869
-- If we add new lua actions to the %%post code we should coordinate
-- with rpm-ostree and ensure that their glibc install is functional.
-- We must not use rpm.execute because this is a RPM 4.15 features and
-- we must still support downstream bootstrap with RPM 4.14 and missing
-- containerized boostrap.

-- Open-code rpm.execute with error message handling.
function post_exec (msg, program, ...)
  if rpm.spawn ~= nil then
    local status = rpm.spawn ({program, ...})
    if status == nil then
      io.stdout:write (msg)
      assert (nil)
    end
  else
    local pid = posix.fork ()
    if pid == 0 then
      posix.exec (program, ...)
      io.stdout:write (msg)
      assert (nil)
    elseif pid > 0 then
      posix.wait (pid)
    end
  end
end

function call_ldconfig ()
  post_exec("Error: call to ldconfig failed.\\n",
	    "ldconfig")
end
}

Name:           glibc%{name_suffix}
Summary:        Standard Shared Libraries (from the GNU C Library)
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-2.1-or-later WITH GCC-exception-2.0
Version:        2.42
Release:        %autorelease
URL:            https://www.gnu.org/software/libc/libc.html
#!RemoteAsset
Source:         https://ftpmirror.gnu.org/gnu/glibc/glibc-%{version}.tar.xz
#!RemoteAsset
Source1:        https://ftpmirror.gnu.org/gnu/glibc/glibc-%{version}.tar.xz.sig
Source5:        nsswitch.conf
# For systemd
Source20:       nscd.conf
Source21:       nscd.service
Source22:       nscd.sysusers

%if %{build_main}
Requires(pre):  filesystem
Recommends:     glibc-extra
Recommends:     glibc-gconv-modules-extra
Provides:       rtld(GNU_HASH)
Provides:       /sbin/ldconfig
%endif
%if %{build_utils}
Requires:       glibc = %{version}
%endif
BuildRequires:  audit-devel
BuildRequires:  bison
BuildRequires:  libcap-devel
BuildRequires:  libselinux-devel
BuildRequires:  texinfo
BuildRequires:  python3
BuildRequires:  systemd-rpm-macros
BuildRequires:  systemtap-sdt-devel
BuildRequires:  xz
%if 0%{?with_gcc:1}
BuildRequires:  gcc%{with_gcc}
%endif
%if %{build_testsuite}
BuildRequires:  gcc%{?with_gcc}-c++
BuildRequires:  gdb
BuildRequires:  glibc-static
BuildRequires:  libidn2-0
BuildRequires:  libstdc++-devel
BuildRequires:  python3-pexpect
%endif
%if %{build_utils}
BuildRequires:  gdb-devel
BuildRequires:  zlib-devel
%endif

Patch100:       glibc-2.4-china.diff

%description
The GNU C Library provides the most important standard libraries used
by nearly all programs: the standard C library, the standard math
library, and the POSIX thread library. A system is not functional
without these libraries.

%package -n glibc-utils
Summary:        Development utilities from the GNU C Library
License:        LGPL-2.1-or-later
Requires:       glibc = %{version}

%description -n glibc-utils
The glibc-utils package contains mtrace, a memory leak tracer and
xtrace, a function call tracer which can be helpful during program
debugging.

If you are unsure if you need this, do not install this package.

%package -n glibc-testsuite
Summary:        Testsuite results from the GNU C Library
License:        LGPL-2.1-or-later

%description -n glibc-testsuite
This package contains the testsuite results from the GNU C Library.

%if %{build_main}

%package info
Summary:        Info Files for the GNU C Library
License:        GFDL-1.1-only
BuildArch:      noarch

%description info
This package contains the documentation for the GNU C library stored as
info files. Due to a lack of resources, this documentation is not
complete and is partially out of date.


%package i18ndata
Summary:        Database Sources for 'locale'
License:        GPL-2.0-or-later AND MIT
BuildArch:      noarch

%description i18ndata
This package contains the data needed to build the locale data files to
use the internationalization features of the GNU libc. It is normally
not necessary to install this packages, the data files are already
created.

%package locale-base
Summary:        en_US Locale Data for Localized Programs
License:        GPL-2.0-or-later AND MIT AND LGPL-2.1-or-later
Requires:       glibc = %{version}

%description locale-base
Locale data for the internationalisation features of the GNU C library.
This package contains only the U.S. English locale.

%package locale
Summary:        Locale Data for Localized Programs
License:        GPL-2.0-or-later AND MIT AND LGPL-2.1-or-later
Requires:       glibc-locale-base = %{version}

%description locale
Locale data for the internationalisation features of the GNU C library.

%package -n nscd
Summary:        Name Service Caching Daemon
License:        GPL-2.0-or-later
Provides:       glibc:/usr/sbin/nscd
Requires:       glibc = %{version}
Obsoletes:      unscd <= 0.48
Requires(pre):  systemd-sysusers
%{?systemd_requires}

%description -n nscd
Nscd caches name service lookups and can dramatically improve
performance with NIS, NIS+, and LDAP.

%package gconv-modules-extra
Summary:        Non-essential gconv modules
License:        LGPL-2.1-or-later
Requires:       glibc = %{version}
Provides:       glibc-locale-base:%{_libdir}/gconv/BIG5.so

%description gconv-modules-extra
Modules for use by the iconv facility, to support encodings other than
Latin-1 and UTF based.

%package devel
Summary:        Include Files and Libraries Mandatory for Development
License:        BSD-3-Clause AND LGPL-2.1-or-later AND LGPL-2.1-or-later WITH GCC-exception-2.0 AND GPL-2.0-or-later
Obsoletes:      epoll = 1.0
Provides:       epoll < 1.0
Requires:       glibc = %{version}
Requires:       libxcrypt-devel
Requires:       linux-headers

%description devel
These libraries are needed to develop programs which use the standard C
library.

%package static
Summary:        C library static libraries for -static linking
License:        BSD-3-Clause AND LGPL-2.1-or-later AND LGPL-2.1-or-later WITH GCC-exception-2.0 AND GPL-2.0-or-later
Requires:       %{name}-devel = %{version}
Requires:       libxcrypt-static
Provides:       %{name}-static = %{version}

%description static
The glibc-static package contains the C library static libraries
for -static linking.  You don't need these, unless you link statically,
which is highly discouraged.

%package extra
# makedb requires libselinux. We add this program in a separate
# package so that glibc does not require libselinux.
Summary:        Extra binaries from GNU C Library
License:        LGPL-2.1-or-later
Requires:       glibc = %{version}

%description extra
The glibc-extra package contains some extra binaries for glibc that
are not essential but recommend for use.

makedb: A program to create a database for nss

%endif

%package -n libnsl1
Summary:        Legacy Network Support Library (NIS)
License:        LGPL-2.1-or-later

%description -n libnsl1
Network Support Library for legacy architectures.  This library does not
have support for IPv6.

%define make_output_sync -Oline

%prep
%autosetup -n glibc-%{version} -p1

%build
# Disable LTO due to a usage of top-level assembler that causes LTO issues
%define _lto_cflags %{nil}
if [ -x /bin/uname.bin ]; then
   /bin/uname.bin -a
else
   uname -a
fi
uptime || :
ulimit -a
nice
# We do not want configure to figure out the system its building one
# to support a common ground and thus set build and host ourself.
target="%{host_arch}-openruyi-linux"
%define build %{_target_cpu}-openruyi-linux
# Default CFLAGS and Compiler
#
enable_stack_protector=
BuildFlags=
tmp="%{optflags}"
for opt in $tmp; do
  case $opt in
    -fstack-protector-*) enable_stack_protector=${opt#-fstack-protector-} ;;
    -fstack-protector) enable_stack_protector=yes ;;
    -D_FORTIFY_SOURCE=*) enable_fortify_source=${opt#-D_FORTIFY_SOURCE=} ;;
    -ffortify=* | *_FORTIFY_SOURCE*) ;;
    *) BuildFlags+=" $opt" ;;
  esac
done
%if 0%{?with_gcc:1}
BuildCC="gcc-%{with_gcc}"
BuildCCplus="g++-%{with_gcc}"
%else
BuildCC="%__cc"
BuildCCplus="%__cxx"
%endif

#
#now overwrite for some architectures
#
%if %{disable_assert}
   BuildFlags="$BuildFlags -DNDEBUG=1"
%endif

#
# Build base glibc
#
mkdir cc-base
cd cc-base

../configure \
   CFLAGS="$BuildFlags" BUILD_CFLAGS="$BuildFlags" \
   CC="$BuildCC" CXX="$BuildCCplus" \
   --prefix=%{_prefix} \
   --libexecdir=%{_libexecdir} --infodir=%{_infodir} \
        $profile \
   --build=%{build} --host=${target} \
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

install -D %{SOURCE22} %{buildroot}%{_sysusersdir}/nscd.conf

%check
%if %{build_testsuite}
export TIMEOUTFACTOR=16
unset MALLOC_CHECK_ MALLOC_PERTURB_
make %{?_smp_mflags} %{?make_output_sync} -C cc-base -k check || {
  cd cc-base
  o=$-
  set +x
  for sum in subdir-tests.sum */subdir-tests.sum; do
    while read s t; do
      case $s in
   XPASS:|PASS:)
     echo ++++++ $s $t ++++++
     ;;
   *) # X?FAIL:
     echo ------ $s $t ------
     test ! -f $t.out || cat $t.out
     ;;
   esac
    done < $sum
  done
  set -$o
  # Fail build if there where compilation errors during testsuite run
  test -f tests.sum
}
%else
# This has to pass on all platforms!
# Exceptions:
# None!
make %{?_smp_mflags} %{?make_output_sync} -C cc-base check-abi
make %{?_smp_mflags} %{?make_output_sync} -C cc-base test t=elf/check-localplt
%endif

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


%define rootsbindir %{_sbindir}
%define slibdir %{_libdir}
%define rtlddir %{_prefix}/%{rtldlib}

%install
%if !%{build_testsuite}

mkdir -p %{buildroot}%{_libdir}
ln -s %{buildroot}%{_libdir} %{buildroot}/%{_lib}
%if "%{rtldlib}" != "%{_lib}"
mkdir -p %{buildroot}%{rtlddir}
ln -s %{buildroot}%{rtlddir} %{buildroot}/%{rtldlib}
%endif
mkdir -p %{buildroot}%{_sbindir}
ln -s %{buildroot}%{_sbindir} %{buildroot}/sbin

%ifarch riscv64
mkdir -p %{buildroot}%{_libdir}
ln -s . %{buildroot}%{_libdir}/lp64d
%if "%{slibdir}" != "%{_libdir}"
mkdir -p %{buildroot}%{slibdir}
ln -s . %{buildroot}%{slibdir}/lp64d
%endif
%endif

%if %{build_main}

# We don't want to strip the .symtab from our libraries in find-debuginfo.sh,
# certainly not from libc.so.* because it is used by libthread_db to find
# some non-exported symbols in order to detect if threading support
# should be enabled.
export STRIP_KEEP_SYMTAB=*.so*

# Install base glibc
%make_install install_root=%{buildroot} -C cc-base

cd cc-base
make %{?_smp_mflags} %{?make_output_sync} install_root=%{buildroot} localedata/install-locale-files
cd ..

rm -rf %{buildroot}%{_datadir}/locale/en_GB/LC_MESSAGES
%find_lang libc --generate-subpackages

install -m 644 %{SOURCE5} %{buildroot}/etc/nsswitch.conf


# nscd tools:

cp nscd/nscd.conf %{buildroot}/etc
mkdir -p %{buildroot}/etc/init.d
ln -sf %{rootsbindir}/service %{buildroot}%{_sbindir}/rcnscd
mkdir -p %{buildroot}/run/nscd
mkdir -p %{buildroot}/var/lib/nscd

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
# Empty the ld.so.cache:
rm -f %{buildroot}/etc/ld.so.cache
touch %{buildroot}/etc/ld.so.cache

# Don't look at ldd! We don't wish a /bin/sh requires
chmod 644 %{buildroot}%{_bindir}/ldd

rm -f %{buildroot}%{rootsbindir}/sln

mkdir -p %{buildroot}/usr/lib/tmpfiles.d/
install -m 644 %{SOURCE20} %{buildroot}/usr/lib/tmpfiles.d/
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 644 %{SOURCE21} %{buildroot}/usr/lib/systemd/system
mkdir -p %{buildroot}/usr/lib/sysusers.d/
install -m 644 %{SOURCE22} %{buildroot}/usr/lib/sysusers.d/nscd.conf

%if 0%{?rtld_oldname:1}
# Provide compatibility link
ln -s %{rtlddir}/%{rtld_name} %{buildroot}%{rtlddir}/%{rtld_oldname}
%endif

# Move getconf to %{_libexecdir}/getconf/ to avoid cross device link
mv %{buildroot}%{_bindir}/getconf %{buildroot}%{_libexecdir}/getconf/getconf
ln -s %{_libexecdir}/getconf/getconf %{buildroot}%{_bindir}/getconf

%if !%{build_utils}
# Remove unwanted files (packaged in glibc-utils)
rm -f %{buildroot}%{slibdir}/libmemusage*
rm -f %{buildroot}%{slibdir}/libpcprofile*
rm -f %{buildroot}%{_bindir}/mtrace
rm -f %{buildroot}%{_bindir}/pcprofiledump
rm -f %{buildroot}%{_bindir}/sotruss
rm -f %{buildroot}%{_bindir}/xtrace
rm -f %{buildroot}%{_bindir}/pldd
rm -rf %{buildroot}%{_libdir}/audit

%endif

%else

%if %{build_utils}

%make_install install_root=%{buildroot} -C cc-base \
  subdirs='malloc debug elf'
cd manpages; make install_root=%{buildroot} install; cd ..
# Remove unwanted files
rm -f %{buildroot}%{rtlddir}/ld*.so* %{buildroot}%{slibdir}/lib[!mp]*
%if "%{_libdir}" != "%{slibdir}"
rm -f %{buildroot}%{_libdir}/lib*
%else
rm -f %{buildroot}%{_libdir}/lib*.a
%endif
rm -f %{buildroot}%{_bindir}/{ld.so,ldd,sprof}
rm -rf %{buildroot}%{_mandir}/man*
rm -rf %{buildroot}%{rootsbindir} %{buildroot}%{_includedir}
%ifarch riscv64
rm %{buildroot}%{_libdir}/lp64d
%if "%{slibdir}" != "%{_libdir}"
rm %{buildroot}%{slibdir}/lp64d
%endif
%endif

%endif

%endif

rm %{buildroot}/%{_lib}
%if "%{rtldlib}" != "%{_lib}"
rm %{buildroot}/%{rtldlib}
%endif
rm %{buildroot}/sbin

%endif

%if %{build_main}

%post -p <lua>

-- First, get rid of platform-optimized libraries. We remove any we have
-- ever built, since otherwise we might end up using some old leftover
-- libraries when new ones aren't installed in their place anymore.
libraries = { "libc.so.6", "libc.so.6.1", "libm.so.6", "libm.so.6.1",
         "librt.so.1", "libpthread.so.0", "libthread_db.so.1" }
remove_dirs = {
  "%{slibdir}/tls/"
}
for i, remove_dir in ipairs(remove_dirs) do
  for j, library in ipairs(libraries) do
    local file = remove_dir .. library
    -- This file could be a symlink to library-%{version}.so, so check
    -- this and don't remove only the link, but also the library itself.
    local link = posix.readlink(file)
    if link then
      if link:sub(1, 1) ~= "/" then link = remove_dir .. link end
      os.remove(link)
    end
    os.remove(file)
  end
end
if posix.access("%{rootsbindir}/ldconfig", "x") then
  rpm.execute("%{rootsbindir}/ldconfig", "-X")
end
if posix.utime("%{_libdir}/gconv/gconv-modules.cache") then
  rpm.execute("%{_sbindir}/iconvconfig", "-o", "%{_libdir}/gconv/gconv-modules.cache",
       "--nostdlib", "%{_libdir}/gconv")
end

%postun -p %{rootsbindir}/ldconfig

%post gconv-modules-extra -p %{_sbindir}/iconvconfig
%postun gconv-modules-extra -p %{_sbindir}/iconvconfig

%pre -n nscd
%sysusers_create_package nscd %{SOURCE22}

%preun -n nscd
%systemd_preun nscd.service

%post -n nscd
%systemd_post nscd.service

%postun -n nscd
%systemd_postun nscd.service
exit 0

# File triggers for when libraries are added or removed in standard
# paths.

%transfiletriggerin -P 2000000 -p <lua> -- /lib /usr/lib /lib64 /usr/lib64
%glibc_post_funcs
call_ldconfig()
%end

%transfiletriggerpostun -P 2000000 -p <lua> -- /lib /usr/lib /lib64 /usr/lib64
%glibc_post_funcs
call_ldconfig()
%end

%files
# glibc
%defattr(-,root,root)
%license LICENSES
%config /etc/ld.so.conf
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
%if "%{slibdir}" != "%{_libdir}"
%{slibdir}/lp64d
%endif
%endif

%{slibdir}/libBrokenLocale.so.1
%{slibdir}/libanl.so.1
%{slibdir}/libc.so.6*
%{slibdir}/libc_malloc_debug.so.0
%{slibdir}/libdl.so.2*
%{slibdir}/libm.so.6*
%{slibdir}/libnss_compat.so.2
%{slibdir}/libnss_db.so.2
%{slibdir}/libnss_dns.so.2
%{slibdir}/libnss_files.so.2
%{slibdir}/libnss_hesiod.so.2
%{slibdir}/libpthread.so.0
%{slibdir}/libresolv.so.2
%{slibdir}/librt.so.1
%{slibdir}/libthread_db.so.1
%{slibdir}/libutil.so.1
%ifarch x86_64
%{_libdir}/libmvec.so.1
%endif
%dir %attr(0700,root,root) /var/cache/ldconfig
%{rootsbindir}/ldconfig
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
%exclude %{_prefix}/lib/locale/C.utf8
%exclude %{_prefix}/lib/locale/en_US.utf8
%exclude %{_prefix}/lib/locale/zh_CN.utf8

%files devel
%defattr(-,root,root)
%license COPYING COPYING.LIB
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
/usr/lib64/libmvec.so
%endif
# These static libraries are needed even for shared builds
%{_libdir}/libc_nonshared.a
%{_libdir}/libdl.a
%{_libdir}/libg.a
%{_libdir}/libmcheck.a
%{_libdir}/libpthread.a
%{_libdir}/librt.a
%{_libdir}/libutil.a

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

%files info
%defattr(-,root,root)
%doc %{_infodir}/libc.info.gz
%doc %{_infodir}/libc.info-?.gz
%doc %{_infodir}/libc.info-??.gz


%files i18ndata
%defattr(-,root,root)
%{_prefix}/share/i18n

%files -n nscd
%defattr(-,root,root)
%config(noreplace) /etc/nscd.conf
%{_sbindir}/nscd
%{_sbindir}/rcnscd
/usr/lib/systemd/system/nscd.service
%dir /usr/lib/tmpfiles.d
/usr/lib/tmpfiles.d/nscd.conf
%dir /usr/lib/sysusers.d
/usr/lib/sysusers.d/nscd.conf
%dir %attr(0755,root,root) %ghost /run/nscd
%attr(0644,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /run/nscd/nscd.pid
%attr(0666,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /run/nscd/socket
%dir %attr(0755,root,root) /var/lib/nscd
%attr(0600,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /var/lib/nscd/passwd
%attr(0600,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /var/lib/nscd/group
%attr(0600,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /var/lib/nscd/hosts
%attr(0600,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /var/lib/nscd/services
%attr(0600,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /var/lib/nscd/netgroup


%files extra
%defattr(-,root,root)
%{_bindir}/makedb
/var/db/Makefile

%files -n libnsl1
%{slibdir}/libnsl.so.1

%endif

%if %{build_utils}
%files -n glibc-utils
%defattr(-,root,root)
%{slibdir}/libmemusage.so
%{slibdir}/libpcprofile.so
%dir %{_libdir}/audit
%{_libdir}/audit/sotruss-lib.so
%{_bindir}/memusage
%{_bindir}/memusagestat
%{_bindir}/mtrace
%{_bindir}/pcprofiledump
%{_bindir}/sotruss
%{_bindir}/xtrace
%{_bindir}/pldd
%endif

%changelog
%{?autochangelog}
