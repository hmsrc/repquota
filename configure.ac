##
# Prologue
##
AC_INIT(m4_esyscmd([awk '/Name:/ {printf "%s",$2; exit}' META]),
        m4_esyscmd([awk '/Version:/ {printf "%s",$2; exit}' META]))
AC_CONFIG_AUX_DIR([config])
AC_CONFIG_SRCDIR([NEWS])
AC_CANONICAL_SYSTEM
X_AC_META
X_AC_EXPAND_INSTALL_DIRS

##
# Automake support
##
AM_INIT_AUTOMAKE($META_NAME, $META_VERSION)
AM_CONFIG_HEADER([config/config.h])
AM_MAINTAINER_MODE

##
# Checks for programs
##
AC_PROG_CC
if test "$GCC" = yes; then
  GCCWARN="-Wall -Wno-unused"
  AC_SUBST([GCCWARN])
  # Lustre libraries are 64-bit only on ppc64
  AC_MSG_CHECKING([whether to force 64-bit mode on ppc64])
  if test x`uname -m` = xppc64 && $CC -v 2>&1 | grep -q biarch; then
    AC_MSG_RESULT([yes])
    CC="$CC -m64"
  else
    AC_MSG_RESULT([no])
  fi
fi

##
# Checks for header files.
##
AC_HEADER_STDC
AC_CHECK_HEADERS( \
  getopt.h \
)

##
# Checks for typedefs, structures, and compiler characteristics
## 
AC_C_BIGENDIAN
AC_C_CONST

##
# Checks for library functions
##
AC_CHECK_FUNCS( \
  getopt_long \
)
AC_SEARCH_LIBS([clnt_create],[nsl])
AC_LUSTRE

##
# For list.c, hostlist.c
##
AC_DEFINE(WITH_LSD_FATAL_ERROR_FUNC, 1, [Define lsd_fatal_error])
AC_DEFINE(WITH_LSD_NOMEM_ERROR_FUNC, 1, [Define lsd_fatal_error])

##
# Epilogue
##
AC_CONFIG_FILES( \
  Makefile \
  rquota.spec \
  src/Makefile \
  test/Makefile \
  man/Makefile \
  man/quota.1 \
  man/quota.conf.5 \
  man/repquota.8 \
  etc/Makefile \
)
AC_OUTPUT
