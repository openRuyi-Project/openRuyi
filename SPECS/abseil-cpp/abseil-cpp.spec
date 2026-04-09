# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           abseil-cpp
Version:        20260107.0
Release:        %autorelease
Summary:        C++ Common Libraries
License:        Apache-2.0 AND LicenseRef-openRuyi-Public-Domain
URL:            https://abseil.io
#!RemoteAsset
Source:         https://github.com/abseil/abseil-cpp/archive/%{version}/%{name}-%{version}.tar.gz
BuildSystem:    cmake

BuildRequires:  cmake
BuildRequires:  ninja
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(gmock)
BuildRequires:  pkgconfig(gtest)

BuildOption(conf):  -GNinja
BuildOption(conf):  -DABSL_USE_EXTERNAL_GOOGLETEST:BOOL=ON
BuildOption(conf):  -DABSL_FIND_GOOGLETEST:BOOL=ON
BuildOption(conf):  -DABSL_ENABLE_INSTALL:BOOL=ON
BuildOption(conf):  -DABSL_BUILD_TESTING:BOOL=ON
BuildOption(conf):  -DABSL_BUILD_TEST_HELPERS:BOOL=ON
BuildOption(conf):  -DCMAKE_BUILD_TYPE:STRING=None
BuildOption(conf):  -DCMAKE_CXX_STANDARD:STRING=17
# TODO: Exclude flaky test. https://github.com/abseil/abseil-cpp/issues/1804
BuildOption(check): --exclude-regex absl_failure_signal_handler_test

# The contents of absl/time/internal/cctz are derived from
# https://github.com/google/cctz (https://src.fedoraproject.org/rpms/cctz), but
# have been forked with Abseil-specific changes. It is not obvious from which
# particular version of CCTZ these sources are derived. Upstream was asked
# about a path to supporting a system copy as required by bundling guidelines:
#   Please comment on CCTZ bundling
#   https://github.com/abseil/abseil-cpp/discussions/1415
# They refused, for the time being, as follows:
#   “[…] we have no plans to change this decision, but we reserve the right to
#   change our minds.”
Provides:       bundled(cctz)

%description
Abseil is an open-source collection of C++ library code designed to augment
the C++ standard library. The Abseil library code is collected from
Google's own C++ code base, has been extensively tested and used in
production, and is the same code we depend on in our daily coding lives.

In some cases, Abseil provides pieces missing from the C++ standard; in
others, Abseil provides alternatives to the standard for special needs we've
found through usage in the Google code base. We denote those cases clearly
within the library code we provide you.

Abseil is not meant to be a competitor to the standard library; we've just
found that many of these utilities serve a purpose within our code base,
and we now want to provide those resources to the C++ community as a whole.

%package        testing
Summary:        Libraries needed for running tests on the installed %{name}
Requires:       %{name} = %{version}-%{release}

Provides:       bundled(cctz)

%description    testing
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-testing = %{version}-%{release}

# Some of the headers from CCTZ are part of the -devel subpackage. See the
# corresponding virtual Provides in the base package for full details.
Provides:       bundled(cctz)

%description    devel
Development headers for %{name}

%files
%global lib_version 2601.0.0
%license LICENSE
%doc FAQ.md README.md UPGRADES.md
# All shared libraries except installed TESTONLY libraries; see the %%files
# list for the -testing subpackage for those.
%{_libdir}/libabsl_base.so.%{lib_version}
%{_libdir}/libabsl_city.so.%{lib_version}
%{_libdir}/libabsl_civil_time.so.%{lib_version}
%{_libdir}/libabsl_cord.so.%{lib_version}
%{_libdir}/libabsl_cord_internal.so.%{lib_version}
%{_libdir}/libabsl_cordz_functions.so.%{lib_version}
%{_libdir}/libabsl_cordz_handle.so.%{lib_version}
%{_libdir}/libabsl_cordz_info.so.%{lib_version}
%{_libdir}/libabsl_cordz_sample_token.so.%{lib_version}
%{_libdir}/libabsl_crc32c.so.%{lib_version}
%{_libdir}/libabsl_crc_cord_state.so.%{lib_version}
%{_libdir}/libabsl_crc_cpu_detect.so.%{lib_version}
%{_libdir}/libabsl_crc_internal.so.%{lib_version}
%{_libdir}/libabsl_debugging_internal.so.%{lib_version}
%{_libdir}/libabsl_decode_rust_punycode.so.%{lib_version}
%{_libdir}/libabsl_demangle_internal.so.%{lib_version}
%{_libdir}/libabsl_demangle_rust.so.%{lib_version}
%{_libdir}/libabsl_die_if_null.so.%{lib_version}
%{_libdir}/libabsl_examine_stack.so.%{lib_version}
%{_libdir}/libabsl_exponential_biased.so.%{lib_version}
%{_libdir}/libabsl_failure_signal_handler.so.%{lib_version}
%{_libdir}/libabsl_flags_commandlineflag.so.%{lib_version}
%{_libdir}/libabsl_flags_commandlineflag_internal.so.%{lib_version}
%{_libdir}/libabsl_flags_config.so.%{lib_version}
%{_libdir}/libabsl_flags_internal.so.%{lib_version}
%{_libdir}/libabsl_flags_marshalling.so.%{lib_version}
%{_libdir}/libabsl_flags_parse.so.%{lib_version}
%{_libdir}/libabsl_flags_private_handle_accessor.so.%{lib_version}
%{_libdir}/libabsl_flags_program_name.so.%{lib_version}
%{_libdir}/libabsl_flags_reflection.so.%{lib_version}
%{_libdir}/libabsl_flags_usage.so.%{lib_version}
%{_libdir}/libabsl_flags_usage_internal.so.%{lib_version}
%{_libdir}/libabsl_graphcycles_internal.so.%{lib_version}
%{_libdir}/libabsl_hash.so.%{lib_version}
%{_libdir}/libabsl_hashtable_profiler.so.%{lib_version}
%{_libdir}/libabsl_hashtablez_sampler.so.%{lib_version}
%{_libdir}/libabsl_int128.so.%{lib_version}
%{_libdir}/libabsl_kernel_timeout_internal.so.%{lib_version}
%{_libdir}/libabsl_leak_check.so.%{lib_version}
%{_libdir}/libabsl_log_flags.so.%{lib_version}
%{_libdir}/libabsl_log_globals.so.%{lib_version}
%{_libdir}/libabsl_log_initialize.so.%{lib_version}
%{_libdir}/libabsl_log_internal_check_op.so.%{lib_version}
%{_libdir}/libabsl_log_internal_conditions.so.%{lib_version}
%{_libdir}/libabsl_log_internal_fnmatch.so.%{lib_version}
%{_libdir}/libabsl_log_internal_format.so.%{lib_version}
%{_libdir}/libabsl_log_internal_globals.so.%{lib_version}
%{_libdir}/libabsl_log_internal_log_sink_set.so.%{lib_version}
%{_libdir}/libabsl_log_internal_message.so.%{lib_version}
%{_libdir}/libabsl_log_internal_nullguard.so.%{lib_version}
%{_libdir}/libabsl_log_internal_proto.so.%{lib_version}
%{_libdir}/libabsl_log_internal_structured_proto.so.%{lib_version}
%{_libdir}/libabsl_log_severity.so.%{lib_version}
%{_libdir}/libabsl_log_sink.so.%{lib_version}
%{_libdir}/libabsl_log_entry.so.%{lib_version}
%{_libdir}/libabsl_malloc_internal.so.%{lib_version}
%{_libdir}/libabsl_periodic_sampler.so.%{lib_version}
%{_libdir}/libabsl_poison.so.%{lib_version}
%{_libdir}/libabsl_profile_builder.so.%{lib_version}
%{_libdir}/libabsl_random_distributions.so.%{lib_version}
%{_libdir}/libabsl_random_internal_distribution_test_util.so.%{lib_version}
%{_libdir}/libabsl_random_internal_entropy_pool.so.%{lib_version}
%{_libdir}/libabsl_random_internal_platform.so.%{lib_version}
%{_libdir}/libabsl_random_internal_randen.so.%{lib_version}
%{_libdir}/libabsl_random_internal_randen_hwaes.so.%{lib_version}
%{_libdir}/libabsl_random_internal_randen_hwaes_impl.so.%{lib_version}
%{_libdir}/libabsl_random_internal_randen_slow.so.%{lib_version}
%{_libdir}/libabsl_random_internal_seed_material.so.%{lib_version}
%{_libdir}/libabsl_random_seed_gen_exception.so.%{lib_version}
%{_libdir}/libabsl_random_seed_sequences.so.%{lib_version}
%{_libdir}/libabsl_raw_hash_set.so.%{lib_version}
%{_libdir}/libabsl_raw_logging_internal.so.%{lib_version}
%{_libdir}/libabsl_scoped_set_env.so.%{lib_version}
%{_libdir}/libabsl_spinlock_wait.so.%{lib_version}
%{_libdir}/libabsl_stacktrace.so.%{lib_version}
%{_libdir}/libabsl_status.so.%{lib_version}
%{_libdir}/libabsl_statusor.so.%{lib_version}
%{_libdir}/libabsl_str_format_internal.so.%{lib_version}
%{_libdir}/libabsl_strerror.so.%{lib_version}
%{_libdir}/libabsl_strings.so.%{lib_version}
%{_libdir}/libabsl_strings_internal.so.%{lib_version}
%{_libdir}/libabsl_borrowed_fixup_buffer.so.%{lib_version}
%{_libdir}/libabsl_generic_printer_internal.so.%{lib_version}
%{_libdir}/libabsl_symbolize.so.%{lib_version}
%{_libdir}/libabsl_synchronization.so.%{lib_version}
%{_libdir}/libabsl_throw_delegate.so.%{lib_version}
%{_libdir}/libabsl_time.so.%{lib_version}
%{_libdir}/libabsl_time_zone.so.%{lib_version}
%{_libdir}/libabsl_tracing_internal.so.%{lib_version}
%{_libdir}/libabsl_utf8_for_code_point.so.%{lib_version}
%{_libdir}/libabsl_vlog_config_internal.so.%{lib_version}

%files testing
# TESTONLY libraries (that are actually installed):
# absl/base/CMakeLists.txt
%{_libdir}/libabsl_exception_safety_testing.so.%{lib_version}
%{_libdir}/libabsl_atomic_hook_test_helper.so.%{lib_version}
%{_libdir}/libabsl_spinlock_test_common.so.%{lib_version}
# absl/container/CMakeLists.txt
%{_libdir}/libabsl_test_instance_tracker.so.%{lib_version}
%{_libdir}/libabsl_hash_generator_testing.so.%{lib_version}
# absl/debugging/CMakeLists.txt
%{_libdir}/libabsl_stack_consumption.so.%{lib_version}
# absl/log/CMakeLists.txt
%{_libdir}/libabsl_log_internal_test_actions.so.%{lib_version}
%{_libdir}/libabsl_log_internal_test_helpers.so.%{lib_version}
%{_libdir}/libabsl_log_internal_test_matchers.so.%{lib_version}
%{_libdir}/libabsl_scoped_mock_log.so.%{lib_version}
# absl/status/CMakeLists.txt
%{_libdir}/libabsl_status_matchers.so.%{lib_version}
# absl/strings/CMakeLists.txt
%{_libdir}/libabsl_pow10_helper.so.%{lib_version}
# absl/synchronization/CMakeLists.txt
%{_libdir}/libabsl_per_thread_sem_test_common.so.%{lib_version}
# absl/time/CMakeLists.txt
%{_libdir}/libabsl_time_internal_test_util.so.%{lib_version}

%files devel
%{_includedir}/absl
%{_libdir}/libabsl_*.so
%{_libdir}/cmake/absl
%{_libdir}/pkgconfig/absl_*.pc

%changelog
%autochangelog
